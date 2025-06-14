from scapy.all import sniff

# Define a callback function that processes each captured packet
def packet_callback(packet):
    print(packet.summary())

# Start sniffing packets
sniff(prn=packet_callback, count=10)
sniff(iface="Wi-Fi", prn=packet_callback, count = 10)