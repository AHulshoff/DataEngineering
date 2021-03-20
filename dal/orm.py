from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey, DateTime, Boolean, Enum, PickleType
from sqlalchemy.orm import mapper, relationship

from dal import model


metadata = MetaData()


class JobStatus(Enum):
    NEW: 0
    PLANNED: 1
    SCHEDULED: 2
    RUNNING: 3
    FINISHED: 4
    FAILED: 9


jobs = Table('Jobs', metadata,
        Column('Id', Integer, primary_key=True, autoincrement=True),
        Column('Name', String(255)),
        Column('Scheduled_Time', DateTime),
        Column('Start_Time', DateTime),
        Column('End_Time', DateTime),
        Column('Success', Boolean),
        Column('Status', Enum(JobStatus))
    )


def start_mappers():
    jobs_mapper = mapper(model.Job, jobs)
