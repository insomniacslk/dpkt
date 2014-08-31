# $Id: udp.py 23 2006-11-08 15:45:33Z dugsong $

"""User Datagram Protocol."""

import dpkt
import dns

UDP_PORT_MAX	= 65535

class UDP(dpkt.Packet):
    __hdr__ = (
        ('sport', 'H', 0xdead),
        ('dport', 'H', 0),
        ('ulen', 'H', 8),
        ('sum', 'H', 0)
        )

    def unpack(self, buf):
        dpkt.Packet.unpack(self, buf)
        if self.sport == 53 or self.dport == 53:
            # Assume it's DNS
            self.data = dns.DNS(self.data)
