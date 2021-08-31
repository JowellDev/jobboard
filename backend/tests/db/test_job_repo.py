from sqlalchemy.orm import Session

from repository.jobs import create_new_job, find_job_by_id
from schemas.jobs import JobSchema
from tests.utils.user import create_random_owner

def test_retreive_job_by_id(db_session: Session):
    title = "test title"
    company = "test comp"
    company_url = "test@test.com"
    location = "Abidjan; CI"
    description = "Bla bla bla bla"
    owner = create_random_owner(db = db_session)
    
    job_schema = JobSchema(
        title = title,
        company = company,
        company_url = company_url,
        location = location,
        description = description,
    )

    new_job = create_new_job(
        job = job_schema, 
        db = db_session,
        owner_id = owner.id
    )

    retreived_job = find_job_by_id(new_job.id, db_session)
    assert retreived_job.id == new_job.id
    assert retreived_job.title == "test title"
