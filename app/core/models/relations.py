from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Index
from sqlalchemy import Table

from .base import Base


"""Incident to Component relation"""
IncidentComponentRelation = Table(
    "incident_component_relation",
    Base.metadata,
    Column("incident_id", ForeignKey("incident.id"), primary_key=True),
    Column("component_id", ForeignKey("component.id"), primary_key=True),
    Index("inc_comp_rel", "incident_id", "component_id", unique=True),
)
