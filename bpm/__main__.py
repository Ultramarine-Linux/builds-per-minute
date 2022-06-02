# set env var
from fedora_messaging import api, config
from .actions import Message
import os
os.environ['FEDORA_MESSAGING_CONF'] = 'my_config.toml'

config.conf.setup_logging()


testdata = {"project": {"id": 251545, "name": "example-package-mte", "homepage": "https://pypi.org/project/example-package-mte/0.0.2", "regex": None, "backend": "PyPI", "version_url": None, "version": "0.0.8", "versions": ["0.0.8", "0.0.7", "0.0.6", "0.0.5", "0.0.4", "0.0.3", "0.0.2", "0.0.1"], "stable_versions": ["0.0.8", "0.0.7", "0.0.6", "0.0.5", "0.0.4", "0.0.3", "0.0.2", "0.0.1"], "created_on": 1654073722.0, "updated_on": 1654080043.0, "ecosystem": "pypi"}, "distro": None, "message": {"project": {"id": 251545, "name": "example-package-mte", "homepage": "https://pypi.org/project/example-package-mte/0.0.2", "regex": None, "backend": "PyPI", "version_url": None, "version": "0.0.8", "versions": [
    "0.0.8", "0.0.7", "0.0.6", "0.0.5", "0.0.4", "0.0.3", "0.0.2", "0.0.1"], "stable_versions": ["0.0.8", "0.0.7", "0.0.6", "0.0.5", "0.0.4", "0.0.3", "0.0.2", "0.0.1"], "created_on": 1654073722.0, "updated_on": 1654080043.0, "ecosystem": "pypi"}, "upstream_versions": ["0.0.7", "0.0.8"], "old_version": "0.0.6", "packages": [], "versions": ["0.0.8", "0.0.7", "0.0.6", "0.0.5", "0.0.4", "0.0.3", "0.0.2", "0.0.1"], "stable_versions": ["0.0.8", "0.0.7", "0.0.6", "0.0.5", "0.0.4", "0.0.3", "0.0.2", "0.0.1"], "ecosystem": "pypi", "agent": "anitya"}}


def track(message):
    action = Message(message.body)
    action.track()


api.consume(track)
