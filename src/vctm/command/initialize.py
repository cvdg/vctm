import datetime
import logging
import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from vctm.chain import Command


class DatabaseCommand(Command):
    def execute(self, context: hash) -> bool:
        """Create a session to the SQLite database"""
        if "db_name" in context:
            db_name = context["db_name"]
        else:
            db_name = os.path.join(context["db_dir"], "vctm.db")
            context["db_name"] = db_name

        engine = create_engine(f"sqlite:///{db_name}", future=True)
        session = Session(engine)

        context["db_engine"] = engine
        context["db_session"] = session

        return Command.SUCCESS

    def post_execute(self, context: hash, success: bool, error: Exception) -> None:
        """Commit or rollback the session"""
        session = context["db_session"]

        if success:
            session.commit()
        else:
            session.rollback()


class DirectoryCommand(Command):
    def execute(self, context: hash) -> bool:
        """Creates the initial directory structure"""
        context["base_dir"] = os.environ.get(
            "VCTM_DIR", os.path.join(Path.home(), "var", "vctm")
        )
        context["db_dir"] = os.path.join(context["base_dir"], "db")
        context["log_dir"] = os.path.join(context["base_dir"], "log")
        context["tmp_dir"] = os.path.join(context["base_dir"], "tmp")

        if not os.path.isdir(context["db_dir"]):
            os.makedirs(context["db_dir"])

        if not os.path.isdir(context["log_dir"]):
            os.makedirs(context["log_dir"])

        if not os.path.isdir(context["tmp_dir"]):
            os.makedirs(context["tmp_dir"])

        return Command.SUCCESS


class LoggingCommand(Command):
    def execute(self, context: hash) -> bool:
        """Configure a basic logging setup"""
        formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)

        if "logfile_name" in context:
            logfile_name = context["logfile_name"]
        else:
            logfile_name = os.path.join(
                context["log_dir"], datetime.datetime.now().strftime("vctm-%Y%m%d.log")
            )
            context["logfile_name"] = logfile_name

        logfile = logging.FileHandler(logfile_name, encoding="UTF-8")
        logfile.setLevel(logging.INFO)
        logfile.setFormatter(formatter)

        root = logging.getLogger()
        root.setLevel(logging.INFO)
        root.addHandler(console)
        root.addHandler(logfile)

        return Command.SUCCESS
