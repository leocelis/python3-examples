#!/usr/bin/env bash

# test connection
curl -X POST -d '{"gremlin":"g.V().limit(10)"}' https://localhost:8182 --insecure

## load data
curl -X POST \
    -H 'Content-Type: application/json' \
    https://localhost:8182/loader -d '
    {
      "source": "s3://test-s3-fo-rings-graph-ext-cat1/gremlin-seed-data/",
      "format": "csv",
      "iamRoleArn": "arn:aws:iam::693973276718:role/NeptuneLoadFromS3",
      "region": "us-west-2",
      "failOnError": "FALSE",
      "parallelism": "MEDIUM",
      "updateSingleCardinalityProperties": "FALSE",
      "queueRequest" : "TRUE"
     }' --insecure

# load status
curl -X GET "https://localhost:8182/loader?errors=TRUE&includeQueuedLoads=TRUE" --insecure

# delete jobs
curl -X DELETE 'https://localhost:8182/loader/c095b02b-ba14-4765-a96c-67f5b7e36109' --insecure
