from pydantic import BaseModel, validator, PositiveInt, ValidationError, IPvAnyAddress
from datetime import datetime
from typing import Optional


class IpAddressSchema(BaseModel):
    ip_address: IPvAnyAddress


class MaltegoSchema(BaseModel):
    ip_address: IPvAnyAddress
    count: int
    now: datetime
