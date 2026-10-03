from scapy.all import sniff, IP, IPv6, TCP, UDP, Raw

print("Starting packet capture...")
print("-" * 60)

def analyze_packet(packet):
    print("\n--- Packet ---")

    # Source and destination IP
    if IP in packet:
        print("Source IP      :", packet[IP].src)
        print("Destination IP :", packet[IP].dst)

    elif IPv6 in packet:
        print("Source IP      :", packet[IPv6].src)
        print("Destination IP :", packet[IPv6].dst)

    # Protocol
    if TCP in packet:
        print("Protocol       : TCP")
    elif UDP in packet:
        print("Protocol       : UDP")
    else:
        print("Protocol       : Other")

    # Packet structure
    print("Packet Layers  :", packet.summary())

    # Payload
    if Raw in packet:
        print("Payload        :", packet[Raw].load)
    else:
        print("Payload        : No readable payload")

print("Capturing 10 packets...")
packets = sniff(count=10, prn=analyze_packet)

print("\nPacket capture completed.")
print("Total packets captured:", len(packets))