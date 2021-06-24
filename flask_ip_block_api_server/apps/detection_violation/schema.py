from pydantic import BaseModel, validator, PositiveInt, ValidationError
from typing import Optional


class DetectionStaticsSchema(BaseModel):
    page_type: str

    @validator('page_type')
    def page_type_in(cls, page_type: str) -> str:
        if page_type not in ['vulnerability', 'suspicious', 'blackip']:
            raise ValueError('page type must in [vulnerability, suspicious, blackip]')
        return page_type


class ViolationStaticsSchema(BaseModel):
    page_type: str

    @validator('page_type')
    def page_type_in(cls, page_type: str) -> str:
        if page_type not in ['vpn', 'tor', 'proxy', 'chinese', 'suspicious_nat', 'remote_access', 'dbconnect', 'snmp',
                             'icmp', 'blocked_policy']:
            raise ValueError(
                'page type must in [vpn, tor, proxy, chinese, suspicious_nat, remote_access, dbconnect, snmp ,icmp, blocked_policy]')
        return page_type
