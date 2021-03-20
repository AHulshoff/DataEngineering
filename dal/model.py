from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from typing import Optional, List, Set
from enum import Enum


class JobStatus(Enum):
    NEW = 0
    PLANNED = 1
    SCHEDULED = 2
    RUNNING = 3
    FINISHED = 4
    FAILED = 9


class NoJob(Exception):
    pass


@dataclass(frozen=False)
class Job:
    Id: int
    Name: str
    Scheduled_Time: datetime
    Start_Time: datetime
    End_Time: datetime
    Status: JobStatus


class DataAccessLayer():

    __job = Job(
            Id=1, 
            Name='TestLoader',
            Scheduled_Time=None,
            Start_Time=None,
            End_Time=None,
            Status=JobStatus.NEW
        )

    def GetJob(self) -> Job:
        if self.__job.Status == JobStatus.NEW:
            self.__job.Scheduled_Time = datetime.now() + timedelta(seconds=10)
            self.__job.Status = JobStatus.PLANNED
            return self.__job
        return None

    def StartJob(self, job: Job):
        job.Start_Time = datetime.now()
        job.Status = JobStatus.RUNNING
        self.__job = job

    def EndJob(self, job: Job):
        job.End_Time = datetime.now()
        job.Status = JobStatus.FINISHED
        self.__job = job

    def FailedJob(self, job: Job):
        job.End_Time = datetime.now()
        job.Status = JobStatus.FAILED
        self.__job = job
