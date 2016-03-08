# _*_ Coding: utf-8 _*_

import socket

def client(message):
    infos = socket.getaddrinfo('127.0.0.1', 5050)
    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    # client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.connect(stream_info[-1])
    client.sendall(message.encode('utf8'))
    buffer_length = 8
    message_complete = False
    message = u''
    while not message_complete:
        part = client.recv(buffer_length)
        message += part.decode('utf8')
        if len(part) < buffer_length:
            message_complete = True
    client.close()
    return message

if __name__ == '__main__':
    client(u'I have written a message.')
