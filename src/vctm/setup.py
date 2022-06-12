import logging


def logger() -> None:
    """ Setup logging. """

    formatter = logging.Formatter(
        '%(asctime)s %(name)s %(levelname)s - %(message)s')

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(logging.INFO)
    root.addHandler(console)
