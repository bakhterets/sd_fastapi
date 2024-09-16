from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base
from .component import Component


class ComponentAttribute(Base):
    """Component Attribute model"""

    __tablename__ = "component_attribute"

    #: Unique identifier for the component attribute
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    #: Foreign key to the component
    component_id: Mapped[int] = mapped_column(
        ForeignKey("component.id"), index=True
    )

    #: Name of the attribute
    name: Mapped[str] = mapped_column(String(30))

    #: Value of the attribute
    value: Mapped[str] = mapped_column(String(50))

    #: Relationship to the component
    component: Mapped[Component] = relationship(back_populates="attributes")

    def __repr__(self):
        """Return a string representation of the component attribute"""
        return "<ComponentAttribute {}={}>".format(self.name, self.value)
