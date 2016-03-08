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
        while server:
            message_complete = False
            message = u""
            while not message_complete:
                part = conn.recv(buffer_length)
                message += part.decode('utf8')
                if len(part) < buffer_length:
                    message_complete = True
            print(message_complete)
            reply(server, message)
    finally: 
        server.close()

def reply(server, message):
    server.sendall(message.encode('utf8'))


if __name__ == '__main__':
    listen_to(server())
  