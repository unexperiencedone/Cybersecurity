import platform
import subprocess

current_os = platform.system()
ip = "184.127.0.1"

if current_os.lower() == "windows":
    ping_cmd = ["ping", "-n", "1", "-w", "2000", ip]
else:
    ping_cmd = ["ping", "-c", "1", "-W", "2", ip]

try:
    result = subprocess.run(ping_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    exit_code = result.returncode
    print(f"Ping Command Output:\n{result.stdout}")
    print(f"Exit Code: {exit_code}")
except Exception as e:
    print(f"Error executing ping command: {e}")
