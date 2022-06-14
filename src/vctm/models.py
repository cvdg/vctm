from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base = declarative_base()


class Organisation(Base):
    __tablename__ = "organisations"
    organisation_id = Column(Integer, primary_key=True)
    name = Column(String(128))
    datetime_created = Column(DateTime(timezone=True),
                              server_default=func.now())
    datetime_updated = Column(DateTime(timezone=True), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('name'),
    )

class Project(Base):
    __tablename__ = "projects"
    organisation_id = Column(Integer, ForeignKey("organisations.organisation_id"), nullable=False)
    project_id = Column(Integer, primary_key=True)
    name = Column(String(128))
    datetime_created = Column(DateTime(timezone=True),
                              server_default=func.now())
    datetime_updated = Column(DateTime(timezone=True), onupdate=func.now())

    organisation = relationship("Organisation")

    __table_args__ = (
        UniqueConstraint('project_id', 'name'),
    )


class Entry(Base):
    __tablename__ = "entries"
    project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)
    entry_id = Column(Integer, primary_key=True)
    title = Column(String(128))
    start = Column(DateTime(timezone=True))
    finish = Column(DateTime(timezone=True))

    datetime_created = Column(DateTime(timezone=True),
                              server_default=func.now())
    datetime_updated = Column(DateTime(timezone=True), onupdate=func.now())

    project = relationship("Project")
