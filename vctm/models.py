
from dataclasses import dataclass, field
import datetime

import logging

_logger = logging.getLogger(__name__)


@dataclass
class Entry:
    title: str
    start: datetime.datetime = field(default_factory=datetime.datetime.now)
    finish: datetime.datetime = None
    description: str = None
    tags: list[str] = field(default_factory=list)


if __name__ == '__main__':
    from vctm.setup import logger

    logger()

    aap = Entry('Aap', tags=['demo', 'aap'])
    noot = Entry('Noot')
    mies = Entry('Mies', tags=['demo', 'mies'])

    print(aap)
    print(noot)
    print(mies)
