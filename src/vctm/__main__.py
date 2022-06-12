
import logging

from vctm.setup import logger as setup_logger

_logger = logging.getLogger(__name__)


def main() -> None:
    setup_logger()

    try:
        _logger.info('main: start')

        raise Exception('dummy')

    except Exception as e:
        _logger.exception(e)
    finally:
        _logger.info('main: finish')


if __name__ == '__main__':
    main()
