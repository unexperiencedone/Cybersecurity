import os 
import platform

current_os = platform.system()
ip = "184.127.129.237"

if current_os.lower() == "windows":
    ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
else:
    ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

exit_code = os.system(ping_cmd)

print(exit_code)

# This is a pingigng syntax in python it commands it to pinbg a certaain ip addreess to check whether it is prone to attacks or not 