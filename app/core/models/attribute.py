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

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    component_id: Mapped[int] = mapped_column(
        ForeignKey("component.id"), index=True
    )
    name: Mapped[str] = mapped_column(String(30))
    value: Mapped[str] = mapped_column(String(50))
    component: Mapped[Component] = relationship(back_populates="attributes")

    def __repr__(self):
        """Return a string representation of the component attribute"""
        return "<ComponentAttribute {}={}>".format(self.name, self.value)
