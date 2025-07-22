from capture_module import list_interfaces, capture_packets
from parser_module import parse_packets
from analyzer_module import analyze_packets
from logger_module import log_results
from visualizer_module import visualize_log


def main():

    list_interfaces()

    interface = input("Enter the interface to capture packets from: ")
    count = int(input("Enter the number of packets to capture: "))

    captured_packets = capture_packets(interface,count)

    parsed_packets = parse_packets(captured_packets)

    analysis_report = analyze_packets(parsed_packets)

    log_file_name = log_results(captured_packets, parsed_packets, analysis_report)

    visualize_log(log_file_name)


if __name__ == "__main__":
    main()