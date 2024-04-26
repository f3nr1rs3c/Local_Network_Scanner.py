from scapy.all import ARP, Ether, srp
import os
from pyfiglet import Figlet
from colorama import init, Fore

# Initialize Colorama
init()

def clear_screen():
    os.system("clear")

# Başlık oluştur
def print_banner():
    f = Figlet(font='slant', width=100)
    print(Fore.GREEN + f.renderText('Connected Devices'))
    print(Fore.RED + "                      | - |  By : F3NR1R - Cyber Security | - |         " + Fore.RESET)

# Ağdaki cihazları keşfetmek için bir ARP isteği paketi oluştur
arp = ARP(pdst="192.168.1.0/24")  # Ağın IP aralığını tanımla

# ARP isteğini kapsayan bir Ethernet çerçevesi oluştur
ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Yayın MAC adresi

# Ethernet çerçevesi ve ARP isteğini birleştir
packet = ether/arp

# Paketi gönder ve cevaplanan cihazların bir listesini al
result = srp(packet, timeout=3, verbose=0)[0]

# Ekranı temizle ve başlığı yazdır
clear_screen()
print_banner()

# Keşfedilen cihazların IP ve MAC adreslerini yazdır
print(Fore.YELLOW + "\nIP Address\t\tMAC Address" + Fore.RESET)
print(Fore.BLUE + "-----------------------------------------" + Fore.RESET)
for sent, received in result:
    print(Fore.MAGENTA + received.psrc + "\t" + received.hwsrc + Fore.RESET)
