import socket

address = input('address: ')
port = int(input('port: '))

sock = socket.socket()

sock.connect((address, port))

while True:
    command = input('> ').strip() + '\n'

    sock.send(command.encode('ascii'))

    if command == 'close\n':
        break

    print(sock.recv(1024).decode('ascii'), end='')

sock.close()
