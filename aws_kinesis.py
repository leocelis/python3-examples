from pprint import pprint
from threading import Thread
from time import sleep

import boto3
import botocore

# configuration
stream_name = 'leocelis_test_stream'
shard_id = 'shardId-000000000000'

# connection
client = boto3.client('kinesis')

# getting streams
print("Listing streams...")
list_streams = client.list_streams()
pprint(list_streams)
print("Describing stream...")
try:
    stream = client.describe_stream(StreamName=stream_name)
    status = stream['StreamDescription']['StreamStatus']
    pprint(stream)

    # if the stream is deleting then wait
    if status == 'DELETING':
        print("Stream is being deleted... please retry in a few seconds")
        exit()

except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == 'ResourceNotFoundException':
        print("Stream not found :(. Let's create it!...")

        # Creating stream
        response = client.create_stream(
            StreamName=stream_name,
            ShardCount=1
        )
        status = 'CREATING'
        while status == 'CREATING':
            print("Stream not ready!... waiting...")
            stream = client.describe_stream(StreamName=stream_name)
            status = stream['StreamDescription']['StreamStatus']
            sleep(5)

        # printing stream
        pprint(stream)


# putting and reading records in parallel
def put_record():
    i = 0
    while 10 > i:
        i += 1
        print("Putting record ({i}) ...".format(i=i))

        client.put_record(
            StreamName=stream_name,
            Data=str.encode("This is Record number {i}".format(i=i)),
            PartitionKey=shard_id,
        )
        sleep(0.5)


# Start writing...
t = Thread(target=put_record)
t.start()

# Start reading...
shard_it = client.get_shard_iterator(
    StreamName=stream_name,
    ShardId=shard_id,
    ShardIteratorType='LATEST'
)
shard_it_key = shard_it['ShardIterator']
while 1 == 1:
    sleep(1)
    print("******** Reading Record ********")
    out = client.get_records(ShardIterator=shard_it_key,
                             Limit=2)
    shard_it_key = out['NextShardIterator']
    pprint(out)
    # abort if no data was found
    if len(out['Records']) == 0:
        break

# delete stream
print("Deleting stream...")
response = client.delete_stream(
    StreamName=stream_name
)
pprint(response)
