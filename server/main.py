import socket
import time

BUFFER = 1024

address = input('address: ')
port = int(input('port: '))

print('. . .')

sock = socket.socket()

sock.bind((address, port))

sock.listen(1)

working = True

while working:
    conn, address = sock.accept()

    while True:
        command = conn.recv(BUFFER).decode('ascii')

        if command == 'close\n':
            working = False
            break

        if command[:4] == 'echo':
            response = command[5:].strip() + '\n'
        elif command[:4] == 'time':
            response = time.ctime() + '\n'
        else:
            response = '\n'

        conn.send(response.encode('ascii'))

    conn.close()
