import socket
import yaml

HOST_NAME = socket.gethostname()

ENV = "LIVE"

with open('core/config.yaml') as f:
    settings = yaml.load(f, Loader=yaml.Loader)
    env_settings = settings[ENV]

G_DATABASE = env_settings['G_DATABASE']
