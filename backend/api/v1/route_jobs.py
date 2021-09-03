from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.jobs import ShowJob, JobSchema
from repository.jobs import create_new_job, find_job_by_id, get_all_jobs, update_a_job, delete_a_job
from api.v1.utils import raise_exception

router = APIRouter()

@router.post('/', response_model=ShowJob)
def create_job(job: JobSchema, db: Session = Depends(get_db)):
    owner_id = 1
    job = create_new_job(job, owner_id, db)
    return job


@router.get('/', response_model=List[ShowJob])
def get_jobs(db: Session = Depends(get_db)):
    jobs = get_all_jobs(db)
    if not jobs:
        print('aucun element !')
    return jobs


@router.get('/{id}', response_model=ShowJob)
def show_job(id: int, db: Session = Depends(get_db)):
    job = find_job_by_id(id, db)
    if not job:
        raise_exception(
            status= status.HTTP_404_NOT_FOUND,
            message= f"Job with index {id} not exist"
        )
    
    return job

@router.put('/{id}')
def update_job(id: int, job: JobSchema, db: Session = Depends(get_db)):
    
    owner_id = 1

    job_found = find_job_by_id(id, db)
    if not job_found:
        raise_exception(
            status= status.HTTP_404_NOT_FOUND,
            message= f"Job with index {id} not exist"
        )
    
    update_a_job(job_found, job, db)
    return {
        "status": status.HTTP_200_OK,
        "msg": "job updated with success"
    }

@router.delete('/{id}')
def delete_job(id: int, db: Session = Depends(get_db)):
    job_found = find_job_by_id(id, db)

    if not job_found:
        raise_exception(
            status= status.HTTP_404_NOT_FOUND,
            message= f"Job with index {id} not exist"
        )

    delete_a_job(job_found, db)
    return {
        "msg": "job deleted with success",
        "status": status.HTTP_200_OK,
    }