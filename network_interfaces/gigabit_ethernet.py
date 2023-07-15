#!/usr/bin/env python

from .netowrk_interface_type import NetworkInterfaceType

class GigabitEthernet(NetworkInterfaceType):
    """
    Gigabit Ethernet Interface class
    """
    def __init__(self) -> None:
        super().__init__()
        self.interface_type = "GigabitEthernet"
