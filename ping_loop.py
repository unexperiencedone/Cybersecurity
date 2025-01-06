import os 
import platform

for i in range(10):
    ip = "192.167.0.{0}".format(i)
    current_platform = platform.system()
    if (current_platform.lower() == "windows"):
        ping_cmd = f"ping -n 1 -w 20 {ip} > nul"
    else:
        ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
    exit_code = os.system(ping_cmd)
    print(exit_code)
    if exit_code == 0:
        print(f"Its online: {ip}")   
    