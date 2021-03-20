from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey, DateTime, Boolean, Enum, PickleType
from sqlalchemy.orm import mapper, relationship
from dal.model import JobStatus, Job


metadata = MetaData()


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
    jobs_mapper = mapper(Job, jobs)
