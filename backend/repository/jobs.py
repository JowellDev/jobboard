from typing import List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from schemas.jobs import JobSchema
from models.jobs import Job
from datetime import datetime

def create_new_job(job: JobSchema, owner_id: int, db: Session):

    new_job = Job(
        **job.dict(),
        date_posted = datetime.now().date(),
        owner_id = owner_id
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job


def find_job_by_id(id: int, db: Session):
    job = db.query(Job).filter(Job.id == id).first()
    return job


def get_all_jobs(db: Session) -> List:
    jobs = db.query(Job).filter(Job.is_active == True).all()
    return jobs


def update_a_job(job_to_update: Job, new_job: JobSchema, db: Session):
    old_data = jsonable_encoder(job_to_update)
    new_data = jsonable_encoder(new_job)

    for field in old_data:
        if field in new_data and new_data[field] != "":
            setattr(job_to_update, field, new_data[field])
    
    db.add(job_to_update)
    db.commit()
    db.refresh(job_to_update)

def delete_a_job(job, db: Session):
    db.delete(job)
    db.commit()
