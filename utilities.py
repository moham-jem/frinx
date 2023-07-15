#!/usr/bin/env python

import json

from exceptions import file_exceptions

from network_interfaces.gigabit_ethernet import GigabitEthernet
from network_interfaces.ten_gigabit_ethernet import TenGigabitEthernet
from network_interfaces.port_channel import PortChannel
#from network_interfaces.bridge_domain_interface import BridgeDomainInterface
#from network_interfaces.loopback import Loopback

FILE_PATH = "./samples/configClear_v2.json"
TOPOLOGY = "frinx-uniconfig-topology:configuration"
INTERFACES_MAPPING = {
#    "BDI": BridgeDomainInterface,
#    "Loopback": Loopback,
    "Port-channel": PortChannel,
    "TenGigabitEthernet": TenGigabitEthernet,
    "GigabitEthernet": GigabitEthernet
}

def get_network_configuration() -> dict:
    """
    Read provided configClear_v2.json and returns it as dictionary
    Returns:
        dict: network configuraiton
    """
    try:
        with open(FILE_PATH, 'r', encoding="utf-8") as file_p:
            content = json.load(file_p)
    except Exception as exc:
        raise file_exceptions.SampleFileException from exc

    return content.get(TOPOLOGY)