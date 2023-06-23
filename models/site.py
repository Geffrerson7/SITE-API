from pydantic import BaseModel


class Site(BaseModel):
    code: str
    name: str
    subproject: str
    sector: str
    latitude: float
    longitude: float
    region: str
    province: str
    district: str
    site_address: str
