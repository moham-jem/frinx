#!/usr/bin/env python

from .database_interface import DatabaseInterface
from .network_interface_table import NetworkInterface
from network_interfaces.netowrk_interface_handler import NetworkInterfaceHandler

class DatabaseHandler:
    """
    Database Handler
    """
    def __init__(self, db: DatabaseInterface) -> None:
        self.db = db

    def save_to_databse(self, i_d:int, network_obj: NetworkInterfaceHandler, interface_type: str) -> None:
        """save to database"""
        self.db.insert(NetworkInterface(
            id=i_d,
            name=network_obj.full_name,
            description=network_obj.description,
            config=network_obj.network_config,
            type=interface_type,
            max_frame_size=network_obj.mtu,
            port_channel_id=network_obj.port_id
        ))
        