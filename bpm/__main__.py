# set env var
from fedora_messaging import api, config
from .actions import Message
from .log import get_logger, ConsoleFormatter
from .git import Git
logger = get_logger(__name__)
import os
#os.environ['FEDORA_MESSAGING_CONF'] = 'my_config.toml'
# set logger to our internal logger
config.conf.load_config("my_config.toml")

def track(message):
    action = Message(message.body)
    action.update()


api.consume(track)
