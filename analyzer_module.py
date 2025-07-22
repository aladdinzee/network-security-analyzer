from capture_module import list_interfaces, capture_packets
from parser_module import parse_packets
from scapy.all import *

################################################################
# This Function analyzes captured packets and provides insights#
################################################################
def analyze_packets(parsed_packets):
    protocol_count = {}
    ip_count = {}
    src_port_count = {}
    dst_port_count = {}

    for pkt in parsed_packets:

        #Count Protcools
        protocol = pkt.get('protocol_name', 'Unknown')
        if protocol in protocol_count:
            protocol_count[protocol] += 1
        else:
            protocol_count[protocol] = 1
        
        #Count IPs
        src_ip = pkt.get('src_ip', 'Unknown')
        dst_ip = pkt.get('dst_ip', 'Unknown')
        if src_ip in ip_count:
            ip_count[src_ip] += 1
        else:
            ip_count[src_ip] = 1
        
        if dst_ip in ip_count:
            ip_count[dst_ip] += 1
        else:
            ip_count[dst_ip] = 1
        
        #Count Ports
        src_port = pkt.get('src_port', 'Unknown')
        dst_port = pkt.get('dst_port', 'Unknown')

        if src_port in src_port_count:
            src_port_count[src_port] += 1
        else:
            src_port_count[src_port] = 1
        
        if dst_port in dst_port_count:
            dst_port_count[dst_port] += 1
        else:
            dst_port_count[dst_port] = 1
        
    # Analysis Report
    report = {
        'protocol_count': protocol_count,
        'ip_count': ip_count,
        'src_port_count': src_port_count,
        'dst_port_count': dst_port_count
    }

    return report