from datetime import datetime
from typing import List
from typing import Optional

from app.datetime import datetime_utcnow

from pydantic import BaseModel
from pydantic import ConfigDict


class ComponentAttributeBase(BaseModel):
    name: str
    value: str
    model_config = ConfigDict(from_attributes=True)


class ComponentBase(BaseModel):
    name: str
    attributes: List[ComponentAttributeBase] = []
    model_config = ConfigDict(from_attributes=True)


class IncidentStatusBase(BaseModel):
    status: str
    text: str
    timestamp: datetime = datetime_utcnow()
    model_config = ConfigDict(from_attributes=True)


class IncidentBase(BaseModel):
    text: str
    impact: int
    start_date: datetime
    end_date: Optional[datetime] = None
    updates: List[IncidentStatusBase] = []
    model_config = ConfigDict(from_attributes=True)


class ComponentCreate(ComponentBase):
    pass


class IncidentComp(IncidentBase):
    id: int


class ComponentRead(ComponentBase):
    id: int
    incidents: List[IncidentComp] = []


class IncidentCreate(IncidentBase):
    components: List[ComponentBase]


class IncidentUpdate(IncidentCreate):
    pass


class IncidentRead(IncidentBase):
    id: int
    components: List[ComponentBase]
