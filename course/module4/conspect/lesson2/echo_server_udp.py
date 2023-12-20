from socket import socket, AF_INET, SOCK_DGRAM


UDP_IP = '127.0.0.1'
UDP_PORT = 8080


def run_server(ip, port):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind((ip, port))
    try:
        while True:
            data, address = sock.recvfrom(1024)
            print(f'Received data: {data.decode("utf-8")} from: {address}')
            sock.sendto(data, address)
            print(f'Sent data: {data.decode("utf-8")} to: {address}')

    except KeyboardInterrupt:
        print(f'Destroy server')
    finally:
        sock.close()


if __name__ == '__main__':
    run_server(UDP_IP, UDP_PORT)
