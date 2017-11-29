import uuid

from redis_helper_functions import cnn
from redis_helper_functions import delete_key
from redis_helper_functions import get_connect
from redis_helper_functions import get_key_value
from redis_helper_functions import increment
from redis_helper_functions import key_exists
from redis_helper_functions import reset_counter
from redis_helper_functions import save_key

# connect to redis
get_connect("localhost")
print(cnn)

# save key
key_name = uuid.uuid4()
print("Key: {}".format(key_name))
redis_key = save_key(key_name, "argentina")

# check if it exists
if key_exists(key_name):
    print("It does exists!")

# get the key value
key_value = get_key_value(key_name)
print(key_value)

# delete key
deleted = delete_key(key_name)
print(deleted)

# check if exists again
if not key_exists(key_name):
    print("It does NOT exists!")

# create a counter
key_name = "pretty_counter"
save_key(key_name, 1)
increment(key_name)
increment(key_name)
increment(key_name)
key_value = get_key_value(key_name)
print(key_value)

# reset the counter
reset_counter(key_name)
key_value = get_key_value(key_name)
print(key_value)
