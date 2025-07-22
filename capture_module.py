from scapy.all import *

################################################################
# This Function lists all available network interfaces         #
################################################################
def list_interfaces():
    interfaces = get_if_list()

    for i, iface in enumerate(interfaces):
        print(f"{i+1} : {iface}")

#################################################################
# This Function captures packets on a specified interface       #
#################################################################
def capture_packets(interface, count):
    print("Starting packet capture...")

    packet = sniff(iface = interface, count = count, store=1)
    
    print("Packet capture complete.")
    return packet