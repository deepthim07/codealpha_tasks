# CodeAlpha Task 1 – Basic Network Packet Sniffer

## Objective

The objective of this task is to build a basic network packet sniffer using Python and Scapy. The program captures network traffic and analyzes packet structure, protocols, source and destination IP addresses, and available payload data.

## Requirements Covered

- Capture network traffic packets
- Analyze captured packets
- Understand basic network protocols and data flow
- Use Scapy for packet capturing
- Display source IP, destination IP, protocols, packet layers, and payloads

## Technologies Used

- Python 3.14.7
- Scapy 2.70
- Npcap 1.89
- Visual Studio Code

## How It Works

The program captures 10 network packets using Scapy's `sniff()` function.

For each captured packet, the program checks:

- Source IP address
- Destination IP address
- Protocol (TCP/UDP)
- Packet layers
- Available raw payload

## Sample Result

The program successfully captured 10 packets and displayed packet information such as Ethernet, IPv4/IPv6, TCP/UDP, and DNS-related traffic.

Some packets may show "No readable payload". This is normal because network packets may contain binary or encrypted data rather than readable text.

## Learning Outcome

This task provided practical experience in network packet capture and analysis. It helped me understand how data travels through a network and how protocols such as IP, TCP, UDP, and DNS are involved in network communication.

## Conclusion

A basic network packet sniffer was successfully developed using Python and Scapy. The program captured and analyzed network packets and displayed useful information about their structure and communication.
