from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from database import metadata

equipment_status = Table('equipment_status',
                         metadata,
                         Column('id', Integer, primary_key=True),
                         Column('status', String, nullable=False)
                         )

equipment = Table('equipment', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('name', String, nullable=False),
                  Column("identifier", String, unique=True, nullable=False),
                  Column("type", String),
                  Column("location", String),
                  Column("status_id", Integer, ForeignKey('equipment_status.id'))
                  )
