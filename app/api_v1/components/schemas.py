from pydantic import BaseModel
from pydantic import ConfigDict


class ComponentBase(BaseModel):
    name: str
    attributes: list[dict]
    incidents: list[dict]


class ComponentCreate(BaseModel):
    pass


class Component(ComponentBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
