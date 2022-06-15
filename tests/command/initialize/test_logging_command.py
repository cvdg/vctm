import logging
import os
import random
import shutil
import string

from vctm.chain import Executor
from vctm.command.initialize import LoggingCommand


def test_logging_command00():
    executor = Executor()
    executor.add_initialize(LoggingCommand())

    name = "".join(random.choice(string.ascii_letters) for i in range(16))

    log_dir = os.path.join("tmp", name)

    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)

    context = {}
    context["log_dir"] = log_dir

    assert executor.execute(context)
    assert "logfile_name" in context

    logging.info("Testing")

    assert os.path.isfile(context["logfile_name"])

    shutil.rmtree(log_dir)
