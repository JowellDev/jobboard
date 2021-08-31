from sqlalchemy.orm import Session
from schemas.jobs import JobSchema
from models.jobs import Job
from datetime import datetime

def create_new_job(job: JobSchema, db: Session):

    new_job = Job(
        title = job.title,
        company = job.company,
        company_url = job.company_url,
        location = job.location,
        description = job.description,
        date_posted = datetime.now().date(),
        #owner_id = 1
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job