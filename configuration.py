import os

default_config = {
    'flask_app': '360 Webview',
    'flask_env': 'development',
    'host': 'localhost',
    'port': 5432,
}

def get_configuration(name):
    return os.environ.get(name, default_config[name])
