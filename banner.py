import socket

def grab_banner(host, port):
    try:
        sock = socket.socket()
        sock.settimeout(3)

        sock.connect((host, port))

        banner = sock.recv(1024).decode().strip()

        sock.close()

        return banner

    except Exception as e:
        return f"Could not grab banner: {e}"
