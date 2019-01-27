import configparser

config = configparser.ConfigParser()
config.read('config.ini')

config.sections()

print(config['bitbucket.org']['User'])

for key in config['bitbucket.org']:
    print(key)
