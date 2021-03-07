from __future__ import print_function  # Python 2/3 compatibility

from gremlin_python import statics
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.structure.graph import Graph
from tornado import httpclient

statics.load_statics(globals())
graph = Graph()

# connect to Neptune
my_req = httpclient.HTTPRequest('wss://localhost:8182/gremlin',
                                # headers={"Authorization": "Token AZX ..."},
                                validate_cert=False)

remoteConn = DriverRemoteConnection(my_req, 'g')
g = graph.traversal().withRemote(remoteConn)

# get who Lauren Weinstein (003A000001fOaGAIA0) knows
r = g.V().has('~id', "003A000001fOaGAIA0").out('knows').last_name.toList()
print("Lauren's contacts")
for i in r:
    print(i)

# get who Lauren's contacts knows
r = g.V().has('~id', "003A000001fOaGAIA0").out('knows').out('knows').last_name.toList()
print("\n\nLauren contacts' contacts")
for i in r:
    print(i)

# get Lauren's contact with RQ > 2
r = g.V().has('~id', "003A000001fOaGAIA0").outE('knows').has('rq', gt(1)).inV().last_name.toList()
print("\n\nLauren's RQ > 1 contacts")
for i in r:
    print(i)

# get Lauren contacts' contacts with RQ > 2
r = g.V().has('~id', "003A000001fOaGAIA0"
              ).outE('knows').has('rq', gt(1)).inV().outE().has('rq', gt(2)).inV().last_name.toList()
print("\n\nLauren's RQ > 1 contacts' contacts with RQ > 2")
for i in r:
    print(i)

# Lauren's path to 003A000001TvO1KIAV
r = g.V().has('~id', "003A000001fOaGAIA0"
              ).repeat(out().simplePath()).until(hasId('003A000001TvO1KIAV')
                                                 ).path().limit(1).unfold().last_name.toList()
print("\n\nLauren's shortest path to Ochoa")
print(r)

# delete all data
# g.V().drop().iterate()

# close connection
remoteConn.close()
