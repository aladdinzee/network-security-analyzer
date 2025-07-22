from capture_module import list_interfaces, capture_packets
from scapy.all import *

################################################################
# This Function parses captured packets and extracts relevant  #
# information.                                                 #
#################################################################
def parse_packets(packets):
    parsed_data = []

    for packet in packets:

        if packet.haslayer(IP):
            ip_layer = packet[IP]
            src_ip = ip_layer.src
            dst_ip = ip_layer.dst
            protocol = ip_layer.proto

            parsed_pkt = {
                'src_ip': src_ip,
                'dst_ip': dst_ip,
                'protocol': protocol,
                'summary': packet.summary()
            }

            if packet.haslayer(TCP):
                parsed_pkt['src_port'] = packet[TCP].sport
                parsed_pkt['dst_port'] = packet[TCP].dport
                parsed_pkt['protocol_name'] = "TCP"
            
            if packet.haslayer(UDP):
                parsed_pkt['src_port'] = packet[UDP].sport
                parsed_pkt['dst_port'] = packet[UDP].dport
                parsed_pkt['protocol_name'] = "UDP"
            
            if packet.haslayer(ICMP):
                parsed_pkt['protocol_name'] = "ICMP"
                parsed_pkt['type'] = packet[ICMP].type
                parsed_pkt['code'] = packet[ICMP].code
            
            parsed_data.append(parsed_pkt)
            
    return parsed_data 