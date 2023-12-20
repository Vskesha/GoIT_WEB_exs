from socket import socket, AF_INET, SOCK_DGRAM


UDP_IP = '127.0.0.1'
UDP_PORT = 8080
MESSAGE = "Python Web development"


def run_client(ip, port):
    sock = socket(AF_INET, SOCK_DGRAM)
    server = ip, port
    for line in MESSAGE.split(' '):
        data = line.encode('utf-8')
        sock.sendto(data, server)
        print(f'Sent data: {data.decode("utf-8")} to: {server}')
        response, address = sock.recvfrom(1024)
        print(f'Received data: {response.decode("utf-8")} from address: {address}')
    sock.close()


if __name__ == '__main__':
    run_client(UDP_IP, UDP_PORT)
