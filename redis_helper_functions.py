from redis import Redis

global cnn
cnn = None


def get_connect(redis_host=None):
    global cnn

    if not redis_host:
        redis_host = "localhost"

    cnn = Redis(host=redis_host)

    return cnn


def save_key(rkey=None, rvalue=None):
    global cnn

    if rkey and rvalue:
        cnn.set(rkey, rvalue)

    return False


def increment(rkey):
    global cnn

    cnn.incr(rkey)

    return True


def reset_counter(rkey=None):
    global cnn

    if rkey:
        rvalue = int(cnn.get(rkey))

        if rvalue and rvalue > 0:
            delete_key(rkey)

            return True

    return False


def delete_key(rkey=None):
    global cnn

    if rkey:
        cnn.delete(rkey)
        return True

    return False


def key_exists(rkey=None):
    global cnn

    rvalue = cnn.get(rkey)

    print(rvalue)

    if rvalue:
        return True

    return False


def get_key_value(rkey=None):
    global cnn

    rvalue = None
    if rkey is not None:
        rvalue = cnn.get(rkey)

    return rvalue
