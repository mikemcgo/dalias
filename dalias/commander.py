import os
import yaml


class Commander:

    def __init__(self, config_path):
        self._config = self._load_config(config_path)

    @staticmethod
    def _load_config(config_path):
        cfg_string = open(config_path, 'r').read()
        try:
            cfg = yaml.safe_load(cfg_string)
        except yaml.YAMLError as e:
            raise CommanderError from e
        return cfg

    def _gen_alias_configs(self):
        base = self._config.pop('base')
        aliases_cfgs = {}
        for cmd, cfg in self._config.items():
            config = dict(base)
            config.update(cfg)
            aliases_cfgs[cmd] = config
        return aliases_cfgs

    def _bash_function(self, args):
        mounts = args.pop('mounts')
        image = args.pop('image')

        arg_str = ' '.join([f'--{arg} {val}' for arg, val in args.items()])
        arg_str = arg_str + ' ' + (' '.join('--volume {source}:{target}'.format(**mount) for mount in mounts))

        return f"docker run {arg_str} {image}"

    def gen_alises(self):
        aliases = {}
        for cmd, args in self._gen_alias_configs().items():
            aliases[cmd] = self._bash_function(args)
        return aliases

class CommanderError(Exception):
    pass
