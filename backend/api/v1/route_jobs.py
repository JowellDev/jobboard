from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.jobs import ShowJob, JobSchema
from repository.jobs import create_new_job, find_job_by_id, get_all_jobs, update_a_job, delete_a_job
from repository.login import get_current_user
from models.users import User

router = APIRouter()

@router.post('/', response_model=ShowJob)
def create_job(job: JobSchema, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    job = create_new_job(job=job, owner_id=current_user.id, db=db)
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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with index {id} not exist"
        )
    
    return job

@router.put('/{id}')
def update_job(id: int, job: JobSchema, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):

    job_found = find_job_by_id(id, db)
    if not job_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with index {id} not exist"
        )
    
    if job_found.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Your are not autorise to update this job post"
        )
    
    update_a_job(job_found, job, db)
    return {
        "status": status.HTTP_200_OK,
        "msg": "job updated with success"
    }

@router.delete('/{id}')
def delete_job(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    job_found = find_job_by_id(id, db)

    if not job_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with index {id} not exist"
        )
    
    if job_found.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Your are not autorise to update this job post"
        )

    delete_a_job(job_found, db)
    return {
        "msg": "job deleted with success",
        "status": status.HTTP_200_OK
    }