# The simplest use case is retrying a flaky function whenever an
# Exception occurs until a value is returned.
import random

from retrying import retry


@retry
def do_something_unreliable():
    if random.randint(0, 10) > 1:
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "Awesome sauce!"


print(do_something_unreliable())


# As you saw above, the default behavior is to retry forever without waiting.
@retry
def never_give_up_never_surrender():
    print("Retry forever ignoring Exceptions, don't wait between retries")


never_give_up_never_surrender()


# Let’s be a little less persistent and set some boundaries, such as the
# number of attempts before giving up.
@retry(stop_max_attempt_number=7)
def stop_after_7_attempts():
    print("Stopping after 7 attempts")


stop_after_7_attempts()


# We don’t have all day, so let’s set a boundary for how long we should
# be retrying stuff.
@retry(stop_max_delay=10000)
def stop_after_10_s():
    print("Stopping after 10 seconds")


stop_after_10_s()


# Most things don’t like to be polled as fast as possible, so let’s just
# wait 2 seconds between retries.
@retry(wait_fixed=2000)
def wait_2_s():
    print("Wait 2 second between retries")


wait_2_s()


# Some things perform best with a bit of randomness injected.
@retry(wait_random_min=1000, wait_random_max=2000)
def wait_random_1_to_2_s():
    print("Randomly wait 1 to 2 seconds between retries")


wait_random_1_to_2_s()


# Then again, it’s hard to beat exponential backoff when retrying distributed
# services and other remote endpoints.
@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000)
def wait_exponential_1000():
    print("Wait 2^x * 1000 milliseconds between each retry, up to 10 seconds, "
          "then 10 seconds afterwards")


wait_exponential_1000()


# We have a few options for dealing with retries that raise specific or
# general exceptions, as in the cases here.
def retry_if_io_error(exception):
    """Return True if we should retry (in this case when it's an IOError),
    False otherwise"""
    return isinstance(exception, IOError)


@retry(retry_on_exception=retry_if_io_error)
def might_io_error():
    print("Retry forever with no wait if an IOError occurs, raise any "
          "other errors")


might_io_error()


@retry(retry_on_exception=retry_if_io_error, wrap_exception=True)
def only_raise_retry_error_when_not_io_error():
    print("Retry forever with no wait if an IOError occurs, raise any other "
          "errors wrapped in RetryError")


only_raise_retry_error_when_not_io_error()


# We can also use the result of the function to alter the behavior of retrying.
def retry_if_result_none(result):
    """Return True if we should retry (in this case when result is None),
    False otherwise"""
    if random.randint(0, 5) > 1:
        return result is None

    return result is True


@retry(retry_on_result=retry_if_result_none,
       wait_exponential_multiplier=1000, wait_exponential_max=10000)
def might_return_none():
    print("Retry forever ignoring Exceptions with no wait if return "
          "value is None")


might_return_none()


# Some things perform best with a bit of randomness injected.
@retry(stop_max_attempt_number=3,
       wait_exponential_multiplier=1000, wait_exponential_max=10000)
def exponential_backoff_exception():
    if random.randint(0, 20) > 1:
        print("Raising exception...")
        raise Exception("Yes, this is an EXCEPTION")

    print("No exceptions. We are good :)")
    return True


try:
    exponential_backoff_exception()
except Exception as e:
    print(e)
