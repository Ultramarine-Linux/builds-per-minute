import os
import toml

# Configuration module

all_configs = []

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = None
        self.setup_logging()
        self.load_config()

    def load_config(self):
        try:
            with open(self.config_file) as f:
                config = toml.load(f)
                # get section called 'bpm'
                self.config = config['bpm']
        except FileNotFoundError:
            print("Config file not found: {}".format(self.config_file))
            exit(1)

global_config = toml.load("config.toml")["bpm-config"]

def load_configs():
    path = os.path.join()
    configs = []
    for f in os.listdir(path):
        if f.endswith(".toml"):
            configs.append(Config(os.path.join(path, f)))
    # merge with all_configs (no duplicates)
    for c in configs:
        if c not in all_configs:
            all_configs.append(c)
        else:
            # replace config with new one
            all_configs[all_configs.index(c)] = c
    return all_configs