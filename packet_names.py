import os
import sys
from time import strftime

""" Exalt Packet Name Dumper

This script will find all incoming, outgoing and data packet names from a given
list of MonoScript files extracted from Exalt. No dependencies required.

Written by him#0001 - find this updated and more here https://github.com/rotmg-nexus/python-scripts
"""

# Folder where the MonoScript files are. Ideally use a folder in the same folder as this script.
directory = "monoscript"

if not os.path.exists(directory):
    print(f"\n[ERROR] Directory '{directory}' does not exist. Please create it manually.")
    sys.exit(-1)

incoming_packets, outgoing_packets = [], []

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)

    if os.path.isfile(filepath):
        with open(filepath, "rb") as file:
            file_contents = file.read()

            # Check if the file is an incoming packet.
            if "DecaGames.RotMG.Net.SocketServer.Messages.Incoming" in str(file_contents) or \
                    "Sources.DecaGames.RotMG.Net.SocketServer.Messages.Incoming" in str(file_contents):
                filename = filename.split('.')[0].split('-')[0]
                incoming_packets.append(filename)
            # Check if the file is an outgoing packet.
            elif "DecaGames.RotMG.Net.SocketServer.Messages.Outgoing" in str(file_contents) or \
                    "Sources.DecaGames.RotMG.Net.SocketServer.Messages.Outgoing" in str(file_contents):
                filename = filename.split('.')[0].split('-')[0]
                outgoing_packets.append(filename)

if len(incoming_packets) == 0 and len(outgoing_packets) == 0:
    print("\n[ERROR] Could not find any packet assets. Is your MonoScript folder empty or file format wrong?")
    sys.exit(-1)

print("\n------ INCOMING ------\n")
for packet in incoming_packets:
    print(packet)

print("\n------ OUTGOING ------\n")
for packet in outgoing_packets:
    print(packet)


# Save packet names to files and print them to the console.

current_time = strftime("%d-%m-%y_%H-%M-%S")
packet_count = len(incoming_packets) + len(outgoing_packets)

print(f"\n[✔] Found {len(incoming_packets)} incoming and {len(outgoing_packets)} outgoing packets ({packet_count} in total)")

# Ask the user if they want to write the names to files.

choice = input("\nWould you like to write the packet names to two txt files? They will be created in the same folder as this script."
               "\nThe files are seperated by packet direction e.g. incoming. The file names are also unique every time this script is run.\n"
               "\nEnter choice (Y/n): ")

if choice.lower() == "y":
    with open(f"incoming_packets_{current_time}.txt", "w") as file:
        for packet in incoming_packets:
            file.write(packet + "\n")
    with open(f"outgoing_packets_{current_time}.txt", "w") as file:
        for packet in outgoing_packets:
            file.write(packet + "\n")

    print(f"\n[✔] Written to 'incoming_packets_{current_time}.txt' and 'outgoing_packets_{current_time}.txt'")
elif choice.lower() == "n":
    pass
else:
    print(f"\nIncorrect choice '{choice}' - enter 'Y' if you would like to save files.")
