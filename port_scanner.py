import socket
from tqdm import tqdm
ports = []
ip = input("Enter IP or domain you want to port scan :")

for port in (pbar :=tqdm(range(1, 65536))):  # Scan ports from 1 to 65535
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Timeout for connection attempt (adjust as needed)
        try:
                pbar.set_description("scanning port {}".format(port))
                s.connect((ip, port))
                print(f"Port {port} is open")
                ports.append(port)
        except socket.error:
                # Connection error means the port is closed or filtered
                pass
        finally:
                s.close()

print("Summary of open ports")
for port in ports:
        print(port)
