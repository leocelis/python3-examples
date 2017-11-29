"""
Find username with the twitter id:
https://tweeterid.com/

Prerequisites
- Create twitter app: https://apps.twitter.com/
- Create Access Token

"""

import json

import oauth2 as oauth

# tweet id
ad_account_id = 'abc123'
tweet_id = 'abc123'

# credentials
# app key and secret
app_consumer_key = 'abc123'
app_consumer_secret = 'abc123'

# account token and secret generated for the app
oauth_token = 'abc123'
oauth_secret = 'abc123'

# get permission of the user related to this ad account
authenticated_user_access_endpoint = \
    "https://ads-api.twitter.com/1/accounts/{account_id}/authenticated_user_access".format(
        account_id=ad_account_id)

# auth library
consumer = oauth.Consumer(key=app_consumer_key, secret=app_consumer_secret)
token = oauth.Token(key=oauth_token, secret=oauth_secret)
client = oauth.Client(consumer, token)

# GET USER PERMS RELATED TO AD ACCOUNT
http_method = "GET"
response, content = client.request(uri=authenticated_user_access_endpoint,
                                   method=http_method)
json_response = json.loads(content.decode('utf-8'))

print("GET {}".format(authenticated_user_access_endpoint))
print("")
print(response)
print("")
print(json_response)
print("")

# POST A TWEET
create_tweet_endpont = "https://api.twitter.com/1.1/statuses/update.json?{p}"
http_method = "POST"
parameters = "status=Test"
post_tweet_url = create_tweet_endpont.format(p=parameters)
response, content = client.request(uri=post_tweet_url,
                                   method=http_method)
json_response = json.loads(content.decode('utf-8'))

print("POST {}".format(post_tweet_url))
print("")
print(response)
print("")
print(json_response)
print("")

# use the tweet recently created, otherwise it will use the one in line #28
if not 'errors' in json_response:
    tweet_id = json_response['id']

# GET A TWEET
get_tweet_endpoint = "https://api.twitter.com/1.1/statuses/show.json?id={id}"
http_method = "GET"
get_tweet_url = get_tweet_endpoint.format(id=tweet_id)
response, content = client.request(uri=get_tweet_url,
                                   method=http_method)
json_response = json.loads(content.decode('utf-8'))

print("GET {}".format(get_tweet_url))
print("")
print(response)
print("")
print(json_response)
print("")

# DELETE A TWEET
delete_tweet_endpoint = "https://api.twitter.com/1.1/statuses/destroy/{id}.json"
http_method = "POST"
delete_tweet_delete = delete_tweet_endpoint.format(id=tweet_id)
response, content = client.request(uri=delete_tweet_delete,
                                   method=http_method)
json_response = json.loads(content.decode('utf-8'))

print("DELETE {}".format(delete_tweet_delete))
print("")
print(response)
print("")
print(json_response)
print("")
