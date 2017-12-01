from html.parser import HTMLParser

import urllib3


class HTMLFindValue(HTMLParser):
    def __init__(self, id: str):
        super().__init__()
        self.id = id
        self._found = False
        self.value = None

    def handle_starttag(self, tag, attr):
        if not self._found and self.id in (str(attr)):
            self._found = True

    def handle_data(self, data):
        if not self.value and self._found and data:
            self.value = data


# get html content
url = 'http://www.nasdaq.com/es/symbol/dis/real-time'
http_pool = urllib3.connection_from_url(url)
r = http_pool.urlopen('GET', url)
html = r.data.decode('utf-8')

# find id in content
id = "qwidget_lastsale"
parser = HTMLFindValue(id=id)
parser.feed(html)
v = parser.value
print(v)
