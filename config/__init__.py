from os.path import join
from configparser import ConfigParser

class Config():

    def __init__(self):
        self.cfg_file_name = join(__name__, 'config.cfg')
        self.config = ConfigParser()
        self.cfg = self.config.read(self.cfg_file_name)
        if len(self.cfg) <= 0:
            self.init_cfg()

    def __getitem__(self, key):
        return self.config[key]

    def init_cfg(self):
        self.config['DEFAULT'] = {
            'debug': 'True',
        }
        self.config['LOGGING'] = {
            'level': 'DEBUG',
        }
        with open(self.cfg_file_name, 'w') as cfg:
            self.config.write(cfg)
