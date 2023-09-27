import logging
import socket
import time

BUFSIZ = 1024

address = input('address: ')
port = int(input('port: '))

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)-8s%(message)s'
    )

print('. . .')

sock = socket.socket()

sock.bind((address, port))

sock.listen(1)

working = True

while working:
    conn, address = sock.accept()
    logging.info(f'accepted {address}')

    while True:
        command = conn.recv(BUFSIZ).decode('ascii')

        if command == 'quit\n':
            break

        if command == 'close\n':
            working = False
            break

        if command[:4] == 'echo':
            logging.info(command.strip())
            response = '\n'.join(command[5:].split()) + '\n'
        elif command[:4] == 'time':
            logging.info(command.strip())
            response = time.ctime() + '\n'
        else:
            logging.warning(f'unknown command \'{command.strip()}\'')
            response = '\n'

        conn.send(response.encode('ascii'))

    logging.info(f'closed {address}')
    conn.close()

sock.close()
