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
    organisation_name = Column(String(128))

    organisation_created = Column(DateTime(timezone=True), server_default=func.now())
    organisation_updated = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    __table_args__ = (UniqueConstraint("organisation_name"),)


class Project(Base):
    __tablename__ = "projects"
    organisation_id = Column(
        Integer, ForeignKey("organisations.organisation_id"), nullable=False
    )
    project_id = Column(Integer, primary_key=True)
    project_name = Column(String(128))
    project_created = Column(DateTime(timezone=True), server_default=func.now())
    project_updated = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    organisation = relationship("Organisation")

    __table_args__ = (UniqueConstraint("organisation_id", "project_name"),)


class Directory(Base):
    __tablename__ = "directories"
    organisation_id = Column(
        Integer, ForeignKey("organisations.organisation_id"), nullable=False
    )
    project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)
    directory_id = Column(Integer, primary_key=True)
    directory_name = Column(String(128))
    directory_created = Column(DateTime(timezone=True), server_default=func.now())
    directory_updated = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    organisation = relationship("Organisation")
    project = relationship("Project")

    __table_args__ = (
        UniqueConstraint("organisation_id", "project_id", "directory_name"),
    )


class Entry(Base):
    __tablename__ = "entries"
    project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)
    entry_id = Column(Integer, primary_key=True)
    entry_name = Column(String(128))
    entry_start = Column(DateTime())
    entry_finish = Column(DateTime())

    entry_created = Column(DateTime(timezone=True), server_default=func.now())
    entry_updated = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    project = relationship("Project")
