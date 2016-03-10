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
        buffer_length = 8
        message_complete = False
        message = b""
        while not message_complete:
            part = conn.recv(buffer_length)
            if part is '':
                message_complete = True
            message += part
            if len(part) < buffer_length:
                message_complete = True
        print(message.decode('utf8'))
        try:
            sending_message = parse_request(message)
            conn.sendall(response_ok())
            conn.sendall(sending_message)
            conn.sendall(b'\r\n\r\n')
        except AttributeError:  # Bad Request
            conn.sendall(response_error(b'405', b'Method Not Allowed'))
        except EnvironmentError:  # Wrong HTTP
            conn.sendall(response_error(b'406', b'Not Acceptable'))
        except NameError:  # No Host
            conn.sendall(response_error(b'400', b'Bad Request'))
        except Exception:  # Any other error
            conn.sendall(response_error(b'500', b'Internal Server Error'))
        finally:
            conn.close()
    except KeyboardInterrupt:
        try:
            conn.close()
        finally:
            print('\nServer Closed')
            server.close()
            quit()

def parse_request(request):
    req_list = request.splitlines()
    header_list = req_list[:req_list.index(b'')]
    if header_list[0][:3] != b'GET':
        raise AttributeError
    if header_list[0][-8:] != b'HTTP/1.1':
        raise EnvironmentError
    for header in header_list[1:]:
        if header[:5] == b'Host:':
            break
    else:
        raise NameError
    return header_list[0][4:-9]


def reply(conn, message):
    conn.sendall(message.encode('utf8'))


def response_ok():
    """return HTTP ok response."""
    return b'HTTP/1.1 200 OK\r\n\r\n'


def response_error(error_code, error_message):
    """return HTTP server error response."""
    return b'HTTP/1.1 {} {}\r\n\r\n'.format(error_code, error_message)


if __name__ == '__main__':
    while True:
        listen_to(server())
