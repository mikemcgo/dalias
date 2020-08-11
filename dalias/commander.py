import docker
import os
import yaml


class Commander:

    def __init__(self, config_path):
        self._config = self._load_config(config_path)

        self._client = docker.client.from_env()

    @staticmethod
    def _load_config(config_path):
        cfg_string = open(config_path, 'r').read()
        for key, value in os.environ.items():
            cfg_string = cfg_string.replace(f'${key.upper()}', value)
        try:
            cfg = yaml.safe_load(cfg_string)
        except yaml.YAMLError as e:
            raise CommanderError from e
        return cfg

    def exec(self, cmd, args):
        if cmd not in self._config:
            raise CommanderError("Command not found")

        conf = self._config.get('base')
        conf.update(self._config[cmd])

        try:
            c = self._client.containers.create(command=args, **conf)

            c.start()
            rc = c.wait()
            print(c.logs().decode("utf-8"))

            # TODO: MAKE THIS OPTIONAL
            c.remove()
            self._client.close()
        except docker.errors.DockerException as e:
            raise CommanderError from e
        return rc.get('StatusCode', 1)

class CommanderError(Exception):
    pass
