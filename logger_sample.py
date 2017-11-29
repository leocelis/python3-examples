import logging.config

import yaml

# yaml config file
log_yaml_file = 'logging/logger_config.yaml'

# read config from yaml
with open(log_yaml_file, 'r') as f:
    log_config_dict = yaml.safe_load(f)
    f.close()

# loading config from yaml file
logging.config.dictConfig(log_config_dict)

# default logging
logging.info("This is info")
logging.warning("This is warning")
logging.critical("This is critical")
logging.debug("This is debug")

# console logging
logger_console = logging.getLogger('log_console')
logger_console.info("Output to the console")
