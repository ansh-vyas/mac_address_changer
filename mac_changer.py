#you can"t become a hacker or programmer by copying and modifying this file. this will make u a cheater 
#author:- ansh vyas
#author instagram :- @_ansh_vyas

import subprocess
import optparse
import re

from pandas import options

def arguments():
    ansh = optparse.OptionParser()
    ansh.add_option("-i","--interface", dest="interface", help="interface to change its mac address")
    ansh.add_option("-nM","--mac", dest="new_mac", help="new mac address")
    (options,arguments) = ansh.parse_args()
    if not options.interface:
        ansh.error("[-] please specify an interface, use --help for full guide.")
    elif not options.new_mac:
        ansh.error("[-] please specify a new mac address, use --help for full guide. ")
    return options

def change_mac(interface, new_mac):
    print(" [-] changing MAC ADDRESS for " + interface + "to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"]) 
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac]) 
    subprocess.call(["ifconfig", interface, "up"])

def current_mac(interface):
    ifconfig_command = subprocess.check_output(["ifconfig", interface])
    mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_command)
    if mac_search:
        return mac_search.group(0)
    else:
        print(" [-] could not find mac address.")

options = arguments()
current_mac_addr = current_mac(options.interface)
print(" [+] current MAC = " + str(current_mac_addr))

change_mac(options.interface, options.new_mac)

current_mac_addr = current_mac(options.interface)
if current_mac_addr == options.new_mac:
    print(" [+] MAC ADDRESS was successully changed to " + current_mac_addr)
else:
    print(" [-] MAC ADDRESS did not get changed.")
