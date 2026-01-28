import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except:
        return False

def main():
    target_ip = input("Enter target IP address: ")
    ports = [21, 22, 23, 80, 443]

    with open("sample_output.txt", "w") as f:
        f.write(f"Scan results for {target_ip}\n")

        for port in ports:
            if scan_port(target_ip, port):
                print(f"Port {port} is OPEN")
                f.write(f"Port {port} is OPEN\n")
            else:
                print(f"Port {port} is CLOSED")
                f.write(f"Port {port} is CLOSED\n")

if __name__ == "__main__":
    main()
