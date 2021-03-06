from typing import Optional
from pydantic import BaseModel
from datetime import date

class JobSchema(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    company_url: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None


class ShowJob(JobSchema):
    date_posted: date
    is_active: bool
    owner_id: int
    class Config():
        orm_mode = True
