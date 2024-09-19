from pydantic import BaseModel
from pydantic import ConfigDict


class ComponentAttributeBase(BaseModel):
    name: str
    value: str
    model_config = ConfigDict(from_attributes=True)


class ComponentAttributeCreate(ComponentAttributeBase):
    pass


class ComponentAttributeRead(ComponentAttributeBase):
    id: int


class ComponentBase(BaseModel):
    name: str
    model_config = ConfigDict(from_attributes=True)


class ComponentCreate(ComponentBase):
    attributes: list[ComponentAttributeCreate]


class ComponentRead(ComponentBase):
    id: int
    attributes: list[ComponentAttributeCreate]
