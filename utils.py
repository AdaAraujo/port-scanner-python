import socket

services = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS"
}

def scan_port(host, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((host, port))
        sock.close()
        return True
    except:
        return False
    
def banner_grabbing(host, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((host, port))
        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = sock.recv(1024)
        sock.close()
        return banner.decode().strip()
    except:
        return None