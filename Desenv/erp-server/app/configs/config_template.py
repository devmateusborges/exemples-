from jinja2 import Environment, FileSystemLoader
import os


env_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'templates'))
env = Environment(
    loader=FileSystemLoader(env_path))

# ======


def configure(app):
    print('>>>Init TEMPLATE')
    app.tpl = env
    return env
