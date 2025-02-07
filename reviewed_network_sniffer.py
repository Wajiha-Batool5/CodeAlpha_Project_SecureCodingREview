from scapy.all import sniff, IP, TCP, UDP, ICMP, get_if_list
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def packet_callback(packet):
    """Callback function to process captured packets."""
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        logging.info(f"Source: {ip_layer.src}, Destination: {ip_layer.dst}")

        # Check for TCP packets
        if TCP in packet:
            tcp_layer = packet[TCP]
            logging.info(f"TCP Packet: {tcp_layer.sport} -> {tcp_layer.dport}")

        # Check for UDP packets
        elif UDP in packet:
            udp_layer = packet[UDP]
            logging.info(f"UDP Packet: {udp_layer.sport} -> {udp_layer.dport}")

        # Check for ICMP packets
        elif ICMP in packet:
            icmp_layer = packet[ICMP]
            logging.info(f"ICMP Packet: Type {icmp_layer.type}, Code {icmp_layer.code}")

def start_sniffer(interface=None):
    """Start sniffing packets on the specified network interface."""
    # Validate the interface
    if interface and interface not in get_if_list():
        logging.error(f"Invalid interface: {interface}")
        return

    logging.info("Starting the network sniffer...")
    try:
        # Start sniffing packets
        sniff(iface=interface, prn=packet_callback, store=0)
    except PermissionError:
        logging.error("Permission denied: You need to run this script with elevated privileges.")
        sys.exit(1)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # You can specify the network interface to sniff on, e.g., 'eth0', 'wlan0', etc.
    # Use None to sniff on all interfaces.
    interface = None  # Change this to your desired interface or keep it None
    start_sniffer(interface)