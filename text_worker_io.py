"""
Description:

This script will parse each file of the given file, extract the first url,
take out the path and querystring and send a request with the same path and
query string to the specified domain.

The domain can have multiple APIs running, and a ports range can be specified.

Usage:

1. Run Flask API:

> python3 rest_apis/rest_api.py

2. Start worker:

> python3 files_io/text_worker_io.py -f 'files_io/urls_list.txt' -d 'http://127.0.0.1' -p '5000:5000'

3. Check output:

> cat files_io/urls_list.txt-results

"""
import argparse
import multiprocessing
import os
import re
import time
from decimal import Decimal
from urllib.parse import urlparse

import requests

start_time = time.time()

# global & contacts
ports = None
current_port = None
URL_REGEX = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))"""


# Functions
def sizeof_fmt(num, suffix='B'):
    """
    Human redable file size

    :param num:
    :param suffix:
    :return:
    """
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def set_and_get_port(ports_list=None):
    """
    Round robin ports range
    :return:
    """
    global current_port
    global ports

    # if port list was sent from command line
    if ports_list:
        # return 2 integers with the port from and port to
        p_from, p_to = [int(p) for p in ports_list.split(":", 1)]
        # creates a range between 2 ports
        ports = list(range(p_from, p_to + 1))

    # if current port is not set or the current port is the last in the list
    if not current_port or len(ports) - 1 == ports.index(current_port):
        # return the first port in range
        current_port = ports[0]
    else:
        # return the next port in range
        current_port = ports[ports.index(current_port) + 1]

    return current_port


def replay_url(domain, path, params):
    port = set_and_get_port()
    url = "{d}:{o}{p}".format(d=domain, o=port, p=path)

    try:
        # time out: connection time and response time
        r = requests.get(url,
                         params=params,
                         timeout=(3, 30))
        return r.text
    except requests.exceptions.RequestException as e:
        print(e)


def extract_url(line):
    """
    Find url in line using regex

    :param line:
    :return:
    """
    urls = re.findall(URL_REGEX, line)

    if len(urls) > 0:
        # only first url found
        url = urls[0]

        # parse url components
        url_parsed = urlparse(url)
        query = url_parsed.query

        # only if querystring exists
        if query:
            if '"' in query:
                query = query.split('"')[0]

            return url_parsed.path, query

    return None, None


def worker(input):
    # extract path and params
    path, query = extract_url(input)

    if path and query:
        # replay to host
        result = replay_url(domain, path, query)
        return result


# Args parser
description = "Replay and store results"
parser = argparse.ArgumentParser(description=description)
parser.add_argument("-f", "--file",
                    type=str,
                    help="path to text file",
                    required=True)
parser.add_argument("-d", "--domain",
                    type=str,
                    help="domain to reply to",
                    required=True)

parser.add_argument("-p", "--ports",
                    type=str,
                    help="port range",
                    required=True)

# Parse args
args = parser.parse_args()
# File to read from
file_read = args.file
# File to write from (autogenerated)
file_write = file_read + "-results"
# Replay host
domain = args.domain
# Ports list
arg_ports = args.ports
set_and_get_port(arg_ports)

# Show file size
statinfo = os.stat(file_read)
file_size = sizeof_fmt(statinfo.st_size)
print("File size: {s}".format(s=file_size))

# Show how many lines
num_lines = len(open(file_read).read().splitlines())
print("File has {n} lines".format(n=num_lines))

# Create Processes Pool
cores = multiprocessing.cpu_count()
pool = multiprocessing.Pool(cores)
print("Creating Pool for {x} cores".format(x=cores))

# Domain + ports
print("Replaying to domain {d} in ports range {r}...".format(d=domain, r=ports))

# iterate through each text line
with open(file_read, mode='r', encoding='utf-8') as input:
    with open(file_write, mode='w', encoding='utf-8') as output:
        # Parallel process lines
        results = pool.map(worker, input)

        # Store results in file
        for result in results:
            if result:
                output.write(result + '\n')

print("DONE!")

# performance calculations
execution_time = time.time() - start_time
print("Execution time: {t} sec".format(t=execution_time))
time_per_request = Decimal(execution_time) / Decimal(num_lines)
print("Avg. time per request: {t} sec".format(t=time_per_request))
