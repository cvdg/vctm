import logging
import logging.handlers
import os
from pathlib import Path


config = {}


def directories(config) -> None:
    """ Setup default directory structure. """

    config['db_dir'] = os.path.join(config['base_dir'], 'db')
    config['log_dir'] = os.path.join(config['base_dir'], 'log')
    config['tmp_dir'] = os.path.join(config['base_dir'], 'tmp')

    if not os.path.isdir(config['db_dir']):
        os.makedirs(config['db_dir'])

    if not os.path.isdir(config['log_dir']):
        os.makedirs(config['log_dir'])

    if not os.path.isdir(config['tmp_dir']):
        os.makedirs(config['tmp_dir'])


def logger(config) -> None:
    """ Setup logging. """

    formatter = logging.Formatter(
        '%(asctime)s %(name)s %(levelname)s - %(message)s')

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    logfile = logging.handlers.TimedRotatingFileHandler(
        config['logfile_name'], when='midnight', backupCount=14, encoding='UTF-8')
    logfile.setLevel(logging.INFO)
    logfile.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(logging.INFO)
    root.addHandler(console)
    root.addHandler(logfile)


def initialize() -> None:
    config['base_dir'] = os.environ.get('VCTM_DIR', os.path.join(Path.home(), 'var', 'vctm'))

    directories(config)

    config['db_name']=os.path.join(config['db_dir'], 'vctm.db')
    config['logfile_name']=os.path.join(config['log_dir'], 'vctm.log')

    logger(config)
