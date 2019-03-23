from urllib.parse import urlsplit, parse_qs

url = "http://www.example.org/default.html?ct=32&op=92&item=98"

# uri components
splitted_url = urlsplit(url)
print("\nscheme: {}".format(splitted_url.scheme))
print("\nnetloc: {}".format(splitted_url.netloc))
print("\npath: {}".format(splitted_url.path))
print("\nquery: {}".format(splitted_url.query))

# querystring
query = splitted_url.query
query_string_mv = parse_qs(query)
query_string_sv = dict({k: v[0] for k, v in query_string_mv.items()})

print("\nParsed query (list values): {}".format(query_string_mv))
print("\nParsed query (single values): {}".format(query_string_sv))
