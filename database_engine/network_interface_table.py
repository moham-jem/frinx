#!/usr/bin/env python

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, JSON

Base = declarative_base()

class NetworkInterface(Base):
    """Network Interface Table"""
    __tablename__ = 'network_interface'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255))
    config = Column(JSON)
    type = Column(String(50))
    max_frame_size = Column(Integer)
    port_channel_id = Column(Integer)