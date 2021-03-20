from datetime import datetime
from dal.model import Job, JobStatus
from loader.loadfactory import LoadFactory
import time
from dal.model import DataAccessLayer 

exec = True
dal = DataAccessLayer()

def Execute(job: Job):
    try:
        dal.StartJob(job)
        proc = LoadFactory.build(job.Name)
        proc.run()
    except:
        dal.FailedJob(job)

job = None
while exec:
    if job != None and job.Status == JobStatus.PLANNED and job.Scheduled_Time >= datetime.now():
        Execute(job)
        dal.EndJob(job)
    else:
        job = dal.GetJob()
    time.sleep(5)


