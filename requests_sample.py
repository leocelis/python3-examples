import requests

# Request with payload and timeout
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

# In timeout the first value is connection time, the second is response time
try:
    r = requests.get('http://www.google.com', params=payload,
                     timeout=(0.1, 0.2))
    print(r.text)
    print(r.url)
except requests.exceptions.RequestException as e:
    print(e)
