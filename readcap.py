# Import the Scapy library
from scapy.all import *

# Get the location of the .cap file from the user
filename = input("Enter the location of the .cap file: ")

# Read the .cap file into a list of packets
packets = rdpcap(filename)

# Loop through each packet in the list
for packet in packets:
    # Print the packet's information to the console
    print(packet.show())
