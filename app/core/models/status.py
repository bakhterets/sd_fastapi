from datetime import datetime
from typing import TYPE_CHECKING

from app.datetime import naive_utcnow

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base


if TYPE_CHECKING:
    from .incident import Incident


class IncidentStatus(Base):
    """Incident Updates"""

    __tablename__ = "incident_status"
    id = mapped_column(Integer, primary_key=True, index=True)
    incident_id = mapped_column(ForeignKey("incident.id"), index=True)
    incident: Mapped["Incident"] = relationship(back_populates="updates")
    timestamp: Mapped[datetime] = mapped_column(
        DateTime, insert_default=naive_utcnow()
    )
    text: Mapped[str] = mapped_column(String())
    status: Mapped[str] = mapped_column(String())
