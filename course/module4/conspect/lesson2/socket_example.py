import socket
from time import sleep
from threading import Thread


def echo_server(host, port):
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        print(f'Connected by {addr}')
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.send(data.upper())


def simple_client(host, port):
    with socket.socket() as s:
        while True:
            try:
                s.connect((host, port))
                s.sendall(b'Hello, world!')
                data = s.recv(1024)
                print(f'From server: {data}')
                break
            except ConnectionRefusedError:
                print('Connection refused')
                sleep(0.5)


HOST = '127.0.0.1'
PORT = 55555

if __name__ == '__main__':
    server = Thread(target=echo_server, args=(HOST, PORT))
    client = Thread(target=simple_client, args=(HOST, PORT))
    server.start()
    client.start()
    server.join()
    client.join()
    print('Done')
