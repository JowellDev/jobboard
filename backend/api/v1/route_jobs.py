from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.jobs import ShowJob, JobSchema
from repository.jobs import create_new_job

router = APIRouter()

@router.post('/', response_model=ShowJob)
def create_job(job: JobSchema, db: Session = Depends(get_db)):
    owner_id = 1
    job = create_new_job(job, db, owner_id)
    return job