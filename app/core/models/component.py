from typing import List
from typing import TYPE_CHECKING

from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base
from .relations import IncidentComponentRelation


if TYPE_CHECKING:
    from .attribute import ComponentAttribute
    from .incident import Incident


class Component(Base):
    """Component model"""

    __tablename__ = "component"

    id = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String())
    attributes: Mapped[List["ComponentAttribute"]] = relationship(
        back_populates="component"
    )
    incidents: Mapped[List["Incident"]] = relationship(
        secondary=IncidentComponentRelation, back_populates="components"
    )

    def __repr__(self):
        return "<Component {}: {}>".format(self.id, self.name)

    def as_string(self, attr_key):
        return "<Component {}: {} ({})>".format(
            self.id, self.name, self.get_attributes_as_dict()[attr_key]
        )
