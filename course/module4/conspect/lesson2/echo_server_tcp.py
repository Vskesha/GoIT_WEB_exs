from socket import socket, AF_INET, SOCK_STREAM
from concurrent.futures import ThreadPoolExecutor


TCP_IP = 'localhost'
TCP_PORT = 8080


def run_server(ip, port):
    def handle(sock: socket, address: str):
        print(f'Connection established {address}')
        while True:
            received, address = sock.recvfrom(1024)
            if not received:
                break
            data = received.decode('utf-8')
            print(f'Received data: {data}')
            sock.send(received)
            print(f'Socket connection closed {address}')
            sock.close()


    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(10)
    print(f'Start echo server {server_socket.getsockname()}')
    with ThreadPoolExecutor(10) as client_pool:
        try:
            while True:
                new_socket, address = server_socket.accept()
                client_pool.submit(handle, new_socket, address)
        except KeyboardInterrupt:
            print(f'Destroy server')
        finally:
            server_socket.close()


if __name__ == '__main__':
    run_server(TCP_IP, TCP_PORT)
