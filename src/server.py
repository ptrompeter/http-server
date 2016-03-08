# _*_ Coding: utf-8 _*_

# _*_ Coding: utf-8 _*_

import socket

def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5050)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(address)
    return server

def listen_to(server):
    try:
        server.listen(1)
        conn, addr = server.accept()
        buffer_length = 1024
<<<<<<< HEAD
        while server:
            message_complete = False
            message = u""
            while not message_complete:
                part = client.recv(buffer_length)
                message += part.decode('utf8')
                if len(part) < buffer_length:
                    message_complete = True
            print(message)
            reply(server, message)
    finally: 
=======
        message_complete = False
        message = u""
        while not message_complete:
            part = conn.recv(buffer_length)
            message += part.decode('utf8')
            if len(part) < buffer_length:
                message_complete = True
        print(message_complete)
        reply(conn, message)
        conn.close()
    except (KeyboardInterrupt, UnboundLocalError):
        print('\nServer Closed')
>>>>>>> 867527b8166ebca8d5ae92c2674447979249e60c
        server.close()
        quit()

def reply(conn, message):
    conn.sendall(message.encode('utf8'))


if __name__ == '__main__':
    try:
        while True:
            listen_to(server())
    except KeyboardInterrupt:
        print('Server Closed')
