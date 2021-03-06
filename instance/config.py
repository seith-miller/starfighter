# /instance/config.py
# This file contains configuration variables that shouldn’t be in version control.
# This includes things like API keys and database URIs containing passwords.
# This also contains variables that are specific to this particular instance of your application.
# For example, you might have DEBUG = False in config.py, but set DEBUG = True in instance/config.py on your local machine 
# for development. Since this file will be read in after config.py, it will override it and set DEBUG = True.

user = "code_user"
password = "my_password"
host = "localhost"
port = "5432"
name = "template1"
