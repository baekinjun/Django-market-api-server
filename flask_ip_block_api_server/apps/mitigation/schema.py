from pydantic import BaseModel, validator, PositiveInt, ValidationError, IPvAnyAddress
from .model import MitigationPageDao
from typing import Optional


class FirewallIpBlockSetSchema(BaseModel):
    fw_id: int
    fw_name: str
    group_name: str
    ip_address: IPvAnyAddress
    requirement_user: str

    @validator('fw_name')
    def fw_name_validation(cls, fw_name: str) -> str:
        tmp = MitigationPageDao().firewall_active((10, 0))
        fw_value = list(map(lambda x: x['fw_name'], tmp))
        if fw_name not in fw_value:
            raise ValueError("fw_name must in {}".format(str(fw_value)))
        return fw_name


class FirewallIpBlockDeleteSchema(BaseModel):
    fw_name: str
    group_name: str
    ip_address: IPvAnyAddress
    requirement_user: str

    @validator('fw_name')
    def fw_name_validation(cls, fw_name: str) -> str:
        tmp = MitigationPageDao().firewall_active((10, 0))
        fw_value = list(map(lambda x: x['fw_name'], tmp))
        if fw_name not in fw_value:
            raise ValueError("fw_name must in {}".format(str(fw_value)))
        return fw_name


class LimitOffsetSchema(BaseModel):
    keyword: str = None
    limit: int
    offset: int


class IpDefinitionWhiteListSetSchema(BaseModel):
    name: str
    description: str
    ip_address: IPvAnyAddress


class IpAddressSchema(BaseModel):
    ip_address: list


class WhiteListDeleteSchema(BaseModel):
    data: list


class BlockHistorySchema(BaseModel):
    category: str = 'all'
    keyword: str = None
    limit: int
    offset: int


class ConfigurationSchema(BaseModel):
    fw_id: int = None
    fw_type: str = None
    fw_name: str = None
    group_name: str = None
    activate_code: int = 0
    dev_id: str = None
    fw_url: IPvAnyAddress = None
    user_id: str = None
    user_pw: str = None
    api_key: str = None


class FwIDSchema(BaseModel):
    fw_id: int
