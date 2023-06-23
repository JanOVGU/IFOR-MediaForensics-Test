import socket
from argparse import ArgumentParser
from pathlib import Path


HOST = "192.168.1.11"
PORT = 80

def client_execute_input(s: socket.socket) -> None:
    while True:
        msg = input("Input Message: ")
        if msg == "exit": break
        s.sendall(msg.encode())

def client_execute_file(s: socket.socket, fp: Path) -> None:
    with open(fp, "wb") as f:
        while data := s.recv(1024):
            f.write(data)

def client_connect() -> socket.socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    return s


def main():
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", type=Path)
    args = parser.parse_args()

    with client_connect() as s:
        if args.file is None:
            client_execute_input(s)
        else:
            client_execute_file(s, args.file)
        input("Press Enter to exit:")

if __name__ == "__main__":
    main()
 
