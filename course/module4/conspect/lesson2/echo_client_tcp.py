from socket import socket, AF_INET, SOCK_STREAM


TCP_IP = 'localhost'
TCP_PORT = 8080
MESSAGE = 'Python Web development'


def run_client(ip, port):
    with socket(AF_INET, SOCK_STREAM) as sock:
        server = ip, port
        sock.connect(server)
        print(f'Connection established {server}')
        for line in MESSAGE.split(' '):
            print(f'Sending data: {line}')
            sock.send(line.encode())
            response = sock.recv(1024)
            print(f'Response data: {response.decode()}')
    print(f'Data transfer completed')


if __name__ == '__main__':
    run_client(TCP_IP, TCP_PORT)
