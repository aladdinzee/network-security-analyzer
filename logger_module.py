import json
from datetime import datetime
from capture_module import list_interfaces, capture_packets
from analyzer_module import analyze_packets
from parser_module import parse_packets

################################################################
# This Function logs the captured packets and analysis results #
################################################################
def log_results(captured_packets, parsed_packets, analysis_report):
    log_data = {
        'timestamp' : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'captured_packets' : [capture.summary() for capture in captured_packets],
        'parsed_packets' : parsed_packets,
        'analysis_report' : analysis_report
    }
    
    ########################################
    #               ALERT                  #
    ########################################
    # The log file should be changed in    #
    # Order to get the latest results.     #
    ########################################

    log_file = f"network_traffic_log.json"

    try:
        with open(log_file, 'a') as file:
            json.dump(log_data, file, indent=4)
        print(f"Results logged to {log_file}")
    except Exception as e:
        print(f"Error logging results: {e}")
    
    return log_file