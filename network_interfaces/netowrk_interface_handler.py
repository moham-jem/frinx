#!/usr/bin/env python

from .netowrk_interface_type import NetworkInterfaceType

class NetworkInterfaceHandler:
    """
    Network Handler
    """
    def __init__(self, network_interface: NetworkInterfaceType, network_config: dict) -> None:
        self.network_interface = network_interface()
        self.network_config = network_config
        self.port_id = None

    @property
    def full_name(self):
        """interface name"""
        return f"{self.network_interface.interface_type}{self.network_config['name']}"

    @property
    def mtu(self):
        """max_frame_size"""
        return self.network_config.get('mtu', None)

    @property
    def description(self):
        """network description"""
        return self.network_config.get('description', "")
