# Python ConfigParser Template
This python project provides a skeleton you can add to your project to take advantage of the Python `ConfigParser`.

## Included
* `config_controller.py`: A module for reading and writing to the ini files. 
* `examples.py`: Examples of how to use/manipulate your configuration file.
* `configuration/app.ini`: An example ini file you can edit to meet your requirements or use as a template for your own configuration files.

## How To Use
1. Clone this repository.
2. Copy the contents into your project.
3. Use the app.ini file as a template to create your own configuration files.
4. Import the `config_controller` module into your application when you need to interact with your configuration files.
5. Look below for a basic example of how to use this skeleton project or `example.py` for more detailed examples. 

## Usage Example
```python
import config_controller

config_file = "app.ini"
app_config = config_controller.init_config(config_file)

# get float value
version_number = app_config.getfloat("about", "version")

# update the log level
app_config.set("log", "log_level", "INFO")

# update the configuration file with the new value
config_controller.save(config_file,app_config)
```
 