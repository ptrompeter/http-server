# _*_ Coding: utf-8 _*_

import socket

def client(message):
    infos = socket.getaddrinfo('127.0.0.1', 5050)
    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.connect(stream_info[-1])
    client.sendall(message.encode('utf8'))
    reply_msg = listen_to(client)
    return reply_msg

def listen_to(client):
    # conn, addr = client.accept()
    buffer_length = 1024
    message_complete = False
    message = u''
    while not message_complete:
        part = client.recv(buffer_length)
        message += part.decode('utf8')
        if len(part) < buffer_length:
            message_complete = True
    client.close()
    return message_complete

if __name__ == '__main__':
    client(u'I have written a message.')
