import socket

address = input('address: ')
port = int(input('port: '))

sock = socket.socket()

sock.connect((address, port))

while True:
    command = input('> ').strip() + '\n'

    if command == 'close\n':
        break

sock.close()
