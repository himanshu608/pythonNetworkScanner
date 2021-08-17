import scapy.all as scapy
import optparse

opt = optparse.OptionParser()

opt.add_option("-i","--iprange",dest="iprange",help="Enter your Ip range to scan eg. 192.168.1.0/24")

(usrinput,arguments) = opt.parse_args()

if not usrinput.iprange:
    print("Please enter Ip range")
else:
    arp_request_packet = scapy.ARP(pdst=usrinput.iprange)

    arp_brodcast_packet = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')

    combined_packet = arp_brodcast_packet / arp_request_packet

    (clients,notfound) = scapy.srp(combined_packet,timeout=1)

    for element in clients:
        print(element[1].psrc + "      " + element[1].hwsrc)
