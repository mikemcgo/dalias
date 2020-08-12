import os
import sys

from dalias.commander import Commander


def commander():
    config_path = os.environ.get('DALIAS_CONFIG_PATH',
                                 '~/dalias/config.json')
    config_path = os.path.expanduser(config_path)

    if not os.path.exists(config_path):
        print(f"Invalid DALIAS_CONFIG_PATH {config_path}")
        sys.exit(1)

    c = Commander(config_path)
    for cmd, alias in c.gen_alises().items():
        print("{}() {{\n {} \"$@\" \n}}".format(cmd, alias))
