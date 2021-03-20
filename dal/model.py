from dal.orm import JobStatus
from enum import Enum
from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional, List, Set


class NoJob(Exception):
    pass


@dataclass(unsafe_hash=True)
class Job:
    Id: int
    Name: str
    Scheduled_Time: datetime
    Start_Time: datetime
    End_Time: datetime
    Success: bool
    Status: JobStatus


