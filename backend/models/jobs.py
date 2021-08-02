from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Text
from sqlalchemy.orm import relationship

from db.base_class import Base

class Job(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(30), nullable=False)
    description = Column(Text, nullable=False)
    company = Column(String(30), nullable=False)
    company_url = Column(String(30), nullable=False)
    location = Column(String(30), nullable=False)
    date_posted = Column(Date)
    is_active = Column(Boolean(), default=True)
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship('User', back_populates='jobs')