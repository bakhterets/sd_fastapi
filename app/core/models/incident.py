from datetime import datetime
from typing import List
from typing import TYPE_CHECKING

from app.datetime import naive_utcnow

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import SmallInteger
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base
from .relations import IncidentComponentRelation


if TYPE_CHECKING:
    from .component import Component
    from .status import IncidentStatus


class Incident(Base):
    """Incident model"""

    __tablename__ = "incident"
    id = mapped_column(Integer, primary_key=True, index=True)
    text: Mapped[str] = mapped_column(String())
    start_date: Mapped[datetime] = mapped_column(
        DateTime, insert_default=naive_utcnow()
    )
    end_date: Mapped[datetime] = mapped_column(nullable=True)
    impact: Mapped[int] = mapped_column(SmallInteger)
    system: Mapped[bool] = mapped_column(Boolean, default=False)
    components: Mapped[List["Component"]] = relationship(
        back_populates="incidents", secondary=IncidentComponentRelation
    )
    updates: Mapped[List["IncidentStatus"]] = relationship(
        back_populates="incident",
        order_by="desc(IncidentStatus.timestamp)",
    )

    def __repr__(self):
        return "<Incident {}: {}>".format(self.id, self.text)
