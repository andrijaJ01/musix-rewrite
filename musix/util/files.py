import os
import toml
config={}
def __ensure__(path):
    if not os.path.isdir(path):
        os.makedirs(path,exist_ok=True)

def read_conf(file=None):
    global config
    if file:
        print(f"reading from config: {file}")
    print("reading from global config file")
    config = toml.load("configs/config.toml")
    return config
