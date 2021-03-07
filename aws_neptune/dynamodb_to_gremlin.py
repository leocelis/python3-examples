"""
Convert DynamoDB Salesforce contact table to Gremlin vertex and edge CSV files
"""
import csv
import json
import random
import uuid

graph_data = list()

# iterate through each DynamoDB table item
f = open("data/dynamodb_table", "r")
for x in f:
    p = json.loads(x)

    # only of owner_id exists the graph can be created
    if 'owner_id' in p:
        salesforce_id = p['salesforce_id']['s']
        first_name = p['first_name']['s']
        last_name = p['last_name']['s']
        owner_id = p['owner_id']['s']
        relationship_quality = p['relationship_quality']['s']

        graph_data.append(
            {
                'salesforce_id': salesforce_id,
                'first_name': first_name,
                'last_name': last_name,
                'owner_id': owner_id,
                'relationship_quality': relationship_quality,
            }
        )

# generate vertex file
vertex_header = ['~id', 'first_name:String', 'last_name:String', '~label']

with open('data/vertex.csv', 'wt', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(i for i in vertex_header)  # write header

    # write vertex data
    for v in graph_data:
        label = "person"
        writer.writerow((v['salesforce_id'], v['first_name'], v['last_name'], label))

# generate edge file
edge_header = ['~id', '~from', '~to', '~label', 'rq:Int']

with open('data/edge.csv', 'wt', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(i for i in edge_header)  # write header

    # write edge data
    for v in graph_data:
        label = 'knows'
        # choose a random contact to build the graph
        graph_density = int(len(graph_data) / 10)
        random_salesforce_id = graph_data[random.randint(0, graph_density)]['salesforce_id']

        writer.writerow(('{}'.format(uuid.uuid1()),
                         # v['owner_id'], # owners don't have a contact associated
                         random_salesforce_id,
                         v['salesforce_id'],
                         label,
                         v['relationship_quality']))
