# The simplest use case is retrying a flaky function whenever an
# Exception occurs until a value is returned.
import random

from retrying import retry


# Some things perform best with a bit of randomness injected.
@retry(stop_max_attempt_number=3,
       wait_exponential_multiplier=1000, wait_exponential_max=10000)
def exponential_backoff_exception():
    value = random.randint(0, 10)
    print("Value {}".format(value))

    if value >= 2:
        print("Raising exception...")
        raise Exception("Yes, this is an EXCEPTION")

    print("No exceptions. We are good :)")
    return True


try:
    exponential_backoff_exception()
except Exception as e:
    print(e)
