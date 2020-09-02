#!/usr/bin/env python3

import subprocess
from getpass import getpass
import optparse
import re

def get_args():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
	parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error("[ERROR] Please define interface using -i or --interface.\nUse --help for more info.\n")
	if not options.new_mac:
		parser.error("[ERROR] Please define mac using -m or --mac.\nUse --help for more info.\n")
	return options

def change_mac(interface, change_to):
	print("\nChanging mac address for %s to %s" % (interface, change_to))
	# normal run bash code
	try:
		# run bash code with sudo password
		subprocess.call(["sudo", "ifconfig", interface, "ether", change_to])
	except:
		print("\nFAILED")

def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig", interface])
	mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
	if mac_address_search_result:
		return mac_address_search_result.group(0)
	else:
		print("Mac address not found!")

options = get_args()
current_mac = get_current_mac(options.interface)
print("\nCurrent MAC: %s" % str(current_mac))

change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:
	print("\nSUCCESS")
else:
	print("MAC address is the same as before.")






