import subprocess

port = input("Enter the port you eant to use: ")
subprocess.run(["C:\\Program Files (x86)\\Nmap\\ncat.exe", "-lvp", port])
# This is  is to create an open server to allow other devices t connect to thjis server