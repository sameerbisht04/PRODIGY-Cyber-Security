from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        protocol = ip_layer.proto
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst

        # Determine protocol type
        protocol_name = {1: "ICMP", 6: "TCP", 17: "UDP"}.get(protocol, "Unknown")

        print(f"Protocol: {protocol_name}")
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print("-" * 50)

# Capture packets
sniff(prn=packet_callback, filter="ip", store=0)
