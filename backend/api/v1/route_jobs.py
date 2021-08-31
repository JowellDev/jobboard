from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.jobs import ShowJob, JobSchema
from repository.jobs import create_new_job, find_job_by_id

router = APIRouter()

@router.post('/', response_model=ShowJob)
def create_job(job: JobSchema, db: Session = Depends(get_db)):
    owner_id = 1
    job = create_new_job(job, db, owner_id)
    return job


@router.get('/{id}', response_model=ShowJob)
def show_job(id: int, db: Session = Depends(get_db)):
    job = find_job_by_id(id, db)
    if not job:
        raise HTTPException(
            detail="no job found !", 
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    return job