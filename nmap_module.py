# # import nmap
# import subprocess
# # the below written code is a simple terminal command to use nmap we will do it fuirther below
# subprocess.run(["nmap", "-p", "127.0.0.1", "8585", "-sT"])
# # We know that nmap can be used to scan ports to find out which port of the device is doing what yet it may be blocked by the firewall and cannot tell us the exact things and sometimes might not provide enough info but it is a certainly a good way

import nmap

port_scan = nmap.PortScanner()
result = port_scan.scan("127.0.0.1", "1111", "-sT")
print(result)

# This is the syntax for the scanning of the port in python it can herlp in determining which one of the prts is open to attacks 