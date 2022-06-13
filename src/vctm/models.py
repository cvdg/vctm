
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base = declarative_base()


class JournalProject(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    datetime_created = Column(DateTime(timezone=True),
                              server_default=func.now())
    datetime_updated = Column(DateTime(timezone=True), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('name'),
    )


tags2entries_table = Table(
    "tags2entries",
    Base.metadata,
    Column("tag_id", ForeignKey("tags.id")),
    Column("entry_id", ForeignKey("entries.id")),
)


class JournalTag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))

    datetime_created = Column(DateTime(timezone=True),
                              server_default=func.now())
    datetime_updated = Column(DateTime(timezone=True), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('name'),
    )


class JournalEntry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True)
    title = Column(String(128))
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    project = relationship("JournalProject")
    start = Column(DateTime(timezone=True))
    finish = Column(DateTime(timezone=True))

    datetime_created = Column(DateTime(timezone=True),
                              server_default=func.now())
    datetime_updated = Column(DateTime(timezone=True), onupdate=func.now())
