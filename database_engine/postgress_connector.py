#!/usr/bin/env python

import sqlalchemy
from sqlalchemy.orm import Session

from .network_interface_table import Base, NetworkInterface
from .database_interface import DatabaseInterface

class PostgressConnector(DatabaseInterface):
    """Postgrsss connection handler"""
    def __init__(self, database: str, user: str, token: str, host: str, port: str) -> None:
        super().__init__()
        self.engine = sqlalchemy.create_engine(f'postgresql+psycopg2://{user}:{token}@{host}:{port}/{database}')
        Base.metadata.create_all(self.engine)

    def insert(self, interface_row: NetworkInterface) -> None:
        """Insert row to DB and commit"""
        with Session(self.engine) as session:
            session.add(interface_row)
            session.commit()
