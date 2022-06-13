import pytest

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from vctm.models import Base
from vctm.models import JournalProject

from vctm.setup import initialize, config

engine = None


@pytest.fixture(autouse=True)
def setup():
    global engine

    initialize()

    engine = create_engine(f'sqlite:///{config["db_name"]}', future=True)
    Base.metadata.create_all(engine)


def test_add_project00():
    # add project Aap
    with Session(engine) as session:
        aap = JournalProject(name='Aap')

        session.add(aap)
        session.commit()

    # check project Aap exist
    with Session(engine) as session:
        aap = session.query(JournalProject).filter(
            JournalProject.name == 'Aap').one()
        session.commit()
        print(aap)

    # delete project Aap
    with Session(engine) as session:
        aap = session.query(JournalProject).filter(
            JournalProject.name == 'Aap').one()
        session.delete(aap)
        session.commit()

    # check project Aap doesn't exist
    with pytest.raises(NoResultFound):
        with Session(engine) as session:
            aap = session.query(JournalProject).filter(
                JournalProject.name == 'Aap').one()
            session.commit()


def test_add_project01():
    # add project Aap
    with Session(engine) as session:
        aap = JournalProject(name='Aap')

        session.add(aap)
        session.commit()

    # add second project Aap
    with pytest.raises(IntegrityError):
        with Session(engine) as session:
            aap = JournalProject(name='Aap')

            session.add(aap)
            session.commit()

    # check project Aap exist
    with Session(engine) as session:
        aap = session.query(JournalProject).filter(
            JournalProject.name == 'Aap').one()
        session.commit()
        print(aap)

    # delete project Aap
    with Session(engine) as session:
        aap = session.query(JournalProject).filter(
            JournalProject.name == 'Aap').one()
        session.delete(aap)
        session.commit()

    # check project Aap doesn't exist
    with pytest.raises(NoResultFound):
        with Session(engine) as session:
            aap = session.query(JournalProject).filter(
                JournalProject.name == 'Aap').one()
            session.commit()


if __name__ == '__name__':
    pytest.main()
