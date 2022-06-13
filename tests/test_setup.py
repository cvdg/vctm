import os
from pathlib import Path

import vctm.setup


# def test_config_empty() -> None:
#     config = vctm.setup.config

#     assert bool(config) == False


def test_config00() -> None:
    os.environ['VCTM_DIR'] = '/tmp/vctm'
    vctm.setup.initialize()
    
    config = vctm.setup.config
    base_dir = '/tmp/vctm'

    assert config['base_dir'] == f'{base_dir}'
    assert config['db_dir'] == f'{base_dir}/db'
    assert config['log_dir'] == f'{base_dir}/log'
    assert config['tmp_dir'] == f'{base_dir}/tmp'
    assert config['db_name'] == f'{base_dir}/db/vctm.db'
    assert config['logfile_name'] == f'{base_dir}/log/vctm.log'

    del os.environ['VCTM_DIR']


def test_config01() -> None:
    vctm.setup.initialize()

    config = vctm.setup.config
    base_dir = os.path.join(Path.home(), 'var', 'vctm')

    assert config['base_dir'] == f'{base_dir}'
    assert config['db_dir'] == f'{base_dir}/db'
    assert config['log_dir'] == f'{base_dir}/log'
    assert config['tmp_dir'] == f'{base_dir}/tmp'
    assert config['db_name'] == f'{base_dir}/db/vctm.db'
    assert config['logfile_name'] == f'{base_dir}/log/vctm.log'
