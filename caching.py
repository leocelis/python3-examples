"""
PEP-0008 = 101.25 KB
Max cache size: 506.25 KB
Max cache elements: 5
TTL in sec: 10
"""
import random
import urllib.request
from copy import deepcopy
from datetime import datetime
from time import sleep

from cachetools import LFUCache

from strings import get_size, convert_size

TTL = 10


def get_pep():
    """Retrieve text of a Python Enhancement Proposal"""
    url = "http://www.python.org/dev/peps/pep-0008/"
    print(url)

    with urllib.request.urlopen(url) as s:
        response = s.read()
        response_size = convert_size(get_size(response))
        print("** Response size: {}".format(response_size))
        return response


def get_elapsed_time(utc_time):
    diff = datetime.utcnow() - utc_time

    return diff.seconds


def expire_items(cached_items):
    cache = deepcopy(cached_items)

    for key, val in cache.items():
        elapsed_time = get_elapsed_time(val[1])

        if elapsed_time >= TTL:
            print("Item {} expired!".format(key))
            del cached_items[key]

    return cached_items


cache = LFUCache(maxsize=5)

n = 0
while True:
    n += 1

    try:
        # remove expired items
        cache = expire_items(cache)

        # cache new item
        cache[n] = get_pep(), datetime.utcnow()

        # randomly access to one element
        random_key = random.choice(range(1, n + 1))

        # if it doens't exist move on
        if random_key not in cache:
            continue

        random_element = cache[random_key]

        print("Randomly accessed to: {}".format(random_key))
        # print("Value for selected element {}".format(cache[random_key]))
        print("All elements cached: {}".format(sorted(cache.keys())))
        print("Total elements cached: {}".format(len(cache)))

        # wait to appreciate the moment
        print()
        sleep(1)
    except urllib.error.HTTPError:
        print('Not Found')
