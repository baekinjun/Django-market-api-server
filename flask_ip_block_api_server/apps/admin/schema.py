from pydantic import BaseModel, validator, PositiveInt, ValidationError
from typing import Optional


class AuditLogSchema(BaseModel):
    category: str = 'all'
    keyword: str = None
    offset: int = 0
    limit: int = 100


class AdminRegisterSchema(BaseModel):
    keyword: str = None
