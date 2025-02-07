from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        print(f"Source: {ip_layer.src}, Destination: {ip_layer.dst}")

        # Check for TCP packets
        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"TCP Packet: {tcp_layer.sport} -> {tcp_layer.dport}")

        # Check for UDP packets
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"UDP Packet: {udp_layer.sport} -> {udp_layer.dport}")

        # Check for ICMP packets
        elif ICMP in packet:
            icmp_layer = packet[ICMP]
            print(f"ICMP Packet: Type {icmp_layer.type}, Code {icmp_layer.code}")

def start_sniffer(interface=None):
    print("Starting the network sniffer...")
    # Start sniffing packets
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    # You can specify the network interface to sniff on, e.g., 'eth0', 'wlan0', etc.
    start_sniffer(interface=None)  # Use None to sniff on all interfaces