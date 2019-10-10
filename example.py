import config_controller
import json


def example_commands():
    # initialise config object using the config_controller
    app_config = config_controller.init_config("app.ini")

    # check section is present
    app_config.has_section("about")

    # check option is present
    app_config.has_option("about", "version")

    # get a list of sections
    app_config.sections()

    # get a list of options
    app_config.options("about")

    # get string value
    app_config.get("updates", "update_url")

    # get float value
    app_config.getfloat("about", "version")

    # get boolean
    app_config.getboolean("updates", "check_for_updates")

    # get int
    app_config.getint("default", "id")

    # get comma separated string  and convert to list
    app_config.get("about", "authors").split(",")

    # get json object and convert to a dict
    json.loads(app_config.get("database", "urls"))

    # remove option
    app_config.remove_option("log", "log_level")

    # remove section
    app_config.remove_section("log")

    # add section to the config file
    app_config.add_section("log")

    # add new value under a section
    app_config.set("log", "log_level", "DEBUG")

    # update value under a section
    app_config.set("log", "log_level", "ERROR")

    # save configuration file
    config_controller.save("app.ini", app_config)


if __name__ == "__main__":
    example_commands()
