"""

How to run it:

> python3 logging/loggers.py
> cat logging/example.log

"""
import logging
import time

logging.basicConfig(filename='logging/example.log',
                    format='%(asctime)s %(name)-8s %(levelname)-8s %(message)s',
                    level=logging.CRITICAL)

logging.debug('Something went wrong! It is OK since this is production')

logging.critical('OMG! this should not happen on production')

time.sleep(1)
