import socket

BUFFER = 1024

address = input('address: ')
port = int(input('port: '))

print('. . .')

sock = socket.socket()

sock.connect((address, port))

while True:
    command = input('> ').strip() + '\n'

    sock.send(command.encode('ascii'))

    if command == 'close\n':
        break

    print(sock.recv(BUFFER).decode('ascii'), end='')

sock.close()
