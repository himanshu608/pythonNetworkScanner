import scapy.all as scapy

arp_request_packet = scapy.ARP(pdst='192.168.101.0/24')

arp_brodcast_packet = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')

combined_packet = arp_brodcast_packet / arp_request_packet

(clients,notfound) = scapy.srp(combined_packet,timeout=1)

for element in clients:
    print(element[1].psrc + "      " + element[1].hwsrc)

