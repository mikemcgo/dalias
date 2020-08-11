import os
import sys

from dalias.commander import Commander


def commander():
    config_path = os.environ.get('DALIAS_CONFIG_PATH',
                                 '~/PycharmProjects/docker_alias/configs/terraform.json')
    config_path = os.path.expanduser(config_path)

    if not os.path.exists(config_path):
        print(f"Invalid DALIAS_CONFIG_PATH {config_path}")
        sys.exit(1)

    if len(sys.argv) == 1:
        print("No alias selected")
        sys.exit(1)
    elif len(sys.argv) > 2:
        args = sys.argv[2:]
    else:
        args = ""

    cmd = sys.argv[1]

    c = Commander(config_path)
    sys.exit(c.exec(cmd, args))

# terraform() {
# docker run --mount type=bind,target=/tmp,source=$PWD --mount type=bind,target=/root,source=$HOME --workdir /tmp hashicorp/terraform:0.12.29
#