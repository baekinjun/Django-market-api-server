from pydantic import BaseModel, validator, PositiveInt, ValidationError
from typing import Optional


class LabIDSchema(BaseModel):
    id: PositiveInt

    @validator('id')
    def limit_id_value(cls, id: int) -> int:
        if id > 3:
            raise ValueError('id value must down 3')
        return id
