import pytest

from vctm.models import Entry


def test_entry_new():
    aap = Entry()
    noot = Entry()
    mies = Entry()

    assert aap is not None
    assert noot is not None
    assert mies is not None


def test_entry_aap():
    aap = Entry(title='aap')

    assert aap.title == 'aap'


def test_entry_noot():
    noot = Entry(title='noot')

    assert noot.title == 'noot'


def test_entry_mies():
    mies = Entry(title='mies')

    assert mies.title == 'mies'


if __name__ == '__main__':
    pytest.main()
