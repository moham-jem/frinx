#!/usr/bin/env python

import utilities

from database_engine.postgress_connector import PostgressConnector
from database_engine.database_handler import DatabaseHandler
from database_engine.network_interface_table import NetworkInterface
from network_configuration.interface_configurations import InterfaceConfiguration
from network_interfaces.netowrk_interface_handler import NetworkInterfaceHandler

def run():
    """
    Run code
    """
    contents = utilities.get_network_configuration()
    interface_types = contents.get(InterfaceConfiguration.CISCO_IOS_XE_NATIVE).get('interface')
    db_handler = DatabaseHandler(
            PostgressConnector(
                database="postgres", user="postgres", token="abc123", host="localhost", port="5432"
            )
        )

    i_d = 1
    for interface_type in interface_types:
        if not interface_type in utilities.INTERFACES_MAPPING:
            continue
        for network_config in interface_types[interface_type]:
            network_obj = NetworkInterfaceHandler(
                network_interface=utilities.INTERFACES_MAPPING[interface_type],
                network_config=network_config
            )
            db_handler.save_to_databse(i_d, network_obj, interface_type)
            i_d += 1
    
if __name__ == "__main__":
    """
    Main Function setup and run
    """
    run()
