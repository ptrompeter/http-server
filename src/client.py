# _*_ coding: utf-8 _*_

import socket
from sys import argv

def client(message):
    infos = socket.getaddrinfo('127.0.0.1', 5050)
    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    client.sendall(message.encode('utf8'))
    buffer_length = 8
    message_complete = False
    message = b''
    while not message_complete:
        part = client.recv(buffer_length)
        if part == '':
                message_complete = True
        message += part
        if len(part) < buffer_length:
            message_complete = True
    client.close()
    return message.decode('utf8')

if __name__ == '__main__':
    script, message = argv
    print(client(message))
