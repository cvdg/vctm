import os
import random
import shutil
import string

from vctm.chain import Command, Executor
from vctm.command.initialize import DatabaseCommand, DirectoryCommand


def test_directory_command00():
    executor = Executor()
    executor.add_initialize(DirectoryCommand())

    name = "".join(random.choice(string.ascii_letters) for i in range(16))
    vctm_dir = os.path.join("tmp", name)
    os.environ["VCTM_DIR"] = vctm_dir

    context = {}

    assert executor.execute(context)
    assert os.path.isdir(os.path.join(vctm_dir, "db"))
    assert os.path.isdir(os.path.join(vctm_dir, "log"))
    assert os.path.isdir(os.path.join(vctm_dir, "tmp"))

    del os.environ["VCTM_DIR"]
    shutil.rmtree(vctm_dir)
