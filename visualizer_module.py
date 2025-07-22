import json
import matplotlib.pyplot as plt
from capture_module import list_interfaces, capture_packets
from analyzer_module import analyze_packets
from parser_module import parse_packets
from logger_module import log_results

################################################################
# This Function visualizes the captured packets and analysis   #
# results using matplotlib.                                    #
################################################################
def visualize_log(log_file_name):
    try:
        with open(log_file_name,'r') as file:
            log_data = json.load(file)

        print(f"Log data loaded from {log_file_name}")

        # Extracting data for visualization 
        protocol_count = log_data.get("analysis_report", {}).get("protocol_count", {})
        ip_count = log_data.get("analysis_report", {}).get("ip_count", {})
        src_port_count = log_data.get("analysis_report", {}).get("src_port_count", {})
        dst_port_count = log_data.get("analysis_report", {}).get("dst_port_count", {})

        # Plotting Protocol Counts
        if protocol_count:
            plt.figure(figsize=(15,10))
            plt.pie(protocol_count.values(), labels=protocol_count.keys(), autopct='%1.2f%%', startangle=140)
            plt.title("Protocol Distribution")
            plt.legend(title="Protocols")

            plt.savefig("protocol_distribution.png", dpi=300, bbox_inches='tight')
        
        # Plotting IP Counts
        if ip_count:
            plt.figure(figsize=(15,10))
            plt.bar(ip_count.keys(), ip_count.values(), color='skyblue')
            plt.xlabel("IP Addresses")
            plt.ylabel("Count")
            plt.title("IP Address Counts")
            plt.xticks(rotation=45)

            plt.savefig("ip_address_counts.png", dpi=300, bbox_inches='tight')
        
        # Plotting Source Port Counts
        if src_port_count:
            plt.figure(figsize=(15,10))
            plt.bar(src_port_count.keys(), src_port_count.values(), color='lightgreen')
            plt.xlabel("Source Ports")
            plt.ylabel("Count")
            plt.title("Source Port Counts")
            plt.xticks(rotation=45)

            plt.savefig("source_port_counts.png", dpi=300, bbox_inches='tight')
            
        # Plotting Destination Port Counts
        if dst_port_count:
            plt.figure(figsize=(15,10))
            plt.bar(dst_port_count.keys(), dst_port_count.values(), color='salmon')
            plt.xlabel("Destination Ports")
            plt.ylabel("Count")
            plt.title("Destination Port Counts")
            plt.xticks(rotation=45)

            plt.savefig("destination_port_counts.png", dpi=300, bbox_inches='tight')

    except:
        print(f"Error loading log file {log_file_name}")
        return