import socket

BUFSIZ = 1024

address = input('address: ')
port = int(input('port: '))

print('. . .')

sock = socket.socket()

sock.connect((address, port))

while True:
    command = ' '.join(input('> ').split()) + '\n'

    if command == '\n':
        continue

    sock.send(command.encode('ascii'))

    if command == 'quit\n' or command == 'close\n':
        break

    print(sock.recv(BUFSIZ).decode('ascii'), end='')

sock.close()
