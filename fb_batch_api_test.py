import pprint

import requests

access_token = "<token>"
url = 'https://graph.facebook.com?access_token={}'.format(access_token)

pp = pprint.PrettyPrinter(indent=4)

batch = '[{"method": "GET","relative_url": "v2.8/6044954761975/insights"}, ' \
        '{"method": "GET","relative_url": "v2.8/insights?ids=[6044954761975,6055255716175]"}]'

data = {
    'batch': batch
}

try:
    r = requests.post(url, json=data)
    pp.pprint(r.json())

except (requests.ConnectionError, requests.Timeout) as e:
    pass
