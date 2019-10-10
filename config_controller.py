from configparser import ConfigParser

config_location = "config/"


def init_config(filename):
    config = ConfigParser(default_section="default")
    config.read(config_location + filename)
    return config


def save(filename, config):
    with open(config_location + filename, 'w') as config_file:
        config.write(config_file)
