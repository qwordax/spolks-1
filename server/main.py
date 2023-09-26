import socket

address = input('address: ')
port = int(input('port: '))

sock = socket.socket()

sock.bind((address, port))

sock.listen(1)

while True:
    print('. . .')
    conn, address = sock.accept()

    conn.close()
