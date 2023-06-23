import socket
from argparse import ArgumentParser
from pathlib import Path


HOST = "192.168.1.11"
PORT = 80


def handle_client(conn: socket.socket, args):
    if args.file is None:
        while True:
            data = conn.recv(1024)
            if not data: break
            print(data.decode())
    else:
        with open(args.file, "rb") as f:
            conn.sendfile(f)

        input("Press Enter to exit:")
        conn.close()

def server_create():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    return s


def main():
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", type=Path)
    args = parser.parse_args()

    with server_create() as s:
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            handle_client(conn, args)

if __name__ == "__main__":
    main()
    
