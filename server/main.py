import socket

address = input('address: ')
port = int(input('port: '))

sock = socket.socket()

sock.bind((address, port))

sock.listen(1)

working = True

while working:
    print('. . .')
    conn, address = sock.accept()

    while True:
        command = conn.recv(1024).decode('ascii')

        if command == 'close\n':
            working = False
            break

        response = command

        conn.send(response.encode('ascii'))

    conn.close()
