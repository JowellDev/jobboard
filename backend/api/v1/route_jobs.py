from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.jobs import ShowJob, JobSchema
from repository.jobs import create_new_job

router = APIRouter()

@router.post('/', response_model=ShowJob)
def create_job(job: JobSchema, owner_id: int, db: Session = Depends(get_db)):
    job = create_new_job(job, db, owner_id)
    return job