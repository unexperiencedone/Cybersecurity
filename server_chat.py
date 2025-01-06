import subprocess

port = input("Enter the port you want to use: ")
subprocess.run(["C:\\Program Files (x86)\\Nmap\\ncat.exe", "-lvp", port])
# This is  is to create an open server to allow other devices to connect to this server
# Now -lvp is a command to execute the server online process ncat is necessary so mention its path its effective to use rather than just ncat because it sometimes does not work
