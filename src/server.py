# _*_ coding: utf-8 _*_

import socket
import io
import pdb
import os.path
import os

RSC = u'webroot{}'

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
            if part is b'':
                message_complete = True
            message += part
            if len(part) < buffer_length:
                message_complete = True
        try:
            body, content_type = resolve_uri(parse_request(message))
            conn.sendall(response_ok() + content_type + b'\r\n\r\n' + body + b'\r\n\r\n')
            # conn.sendall(content_type)
            # conn.sendall(b'\r\n\r\n')
            # conn.sendall(body)
            # conn.sendall(b'\r\n\r\n')
        except AttributeError:  # Bad Request
            conn.sendall(response_error(u'405', u'Method Not Allowed'))
        except TypeError:  # Wrong HTTP
            conn.sendall(response_error(u'406', u'Not Acceptable'))
        except NameError:  # No Host
            conn.sendall(response_error(u'400', u'Bad Request'))
        except IOError:  # Requested file not found.
            conn.sendall(response_error(u'404', u'Resource Not Found'))
        except Exception:  # Any other error
            conn.sendall(response_error(u'500', u'Internal Server Error'))
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
    """Parse request and validate"""
    req_list = request.splitlines()
    header_list = req_list[:req_list.index(b'')]
    if header_list[0][:3] != b'GET':
        raise AttributeError
    if header_list[0][-8:] != b'HTTP/1.1':
        raise TypeError
    for header in header_list[1:]:
        if header[:5] == b'Host:':
            break
    else:
        raise NameError
    return header_list[0][4:-9].strip()


def resolve_uri(uri):
    req_path = RSC.format(uri.decode('utf8'))
    try:
        #pdb.set_trace()
        if os.path.isdir(req_path):
            target = html_maker(req_path, uri)
            return (target, b'Content-Type: text/html')
        f = io.open(req_path, 'rb')
        target = f.read()
        f.close()
    except IOError:
        raise IOError
    uri_suffix = uri[-uri[::-1].index(b'.'):]
    content_type = b'Content-Type: '
    if uri_suffix == b'txt':
        content_type += b'text/plain'
    elif uri_suffix == b'jpg' or uri_suffix == b'.jpeg':
        content_type += b'image/jpeg'
    elif uri_suffix == b'html':
        content_type += b'text/html'
    elif uri_suffix == b'png':
        content_type += b'image/png'
    elif uri_suffix == b'py':
        content_type += b'text/python'
    else:
        raise IOError
    return(target, content_type)

def html_maker(req_path, uri):
    anchors = u''
    html_base = u'<!DOCTYPE html><html><body>{}</body></html>'
    d_format = u'<a href="{root}{file_name}/">{file_name}</a><br>'
    f_format = u'<a href="{root}{file_name}">{file_name}</a><br>'
    for root, dirs, files in os.walk(req_path):
        for d in dirs:
            anchors += d_format.format(root=uri.decode('utf-8'), file_name=d)
        for f in files:
            anchors += f_format.format(root=uri.decode('utf-8'), file_name=f)
    return html_base.format(anchors).encode('utf-8')


def reply(conn, message):
    conn.sendall(message.encode('utf8'))


def response_ok():
    """return HTTP ok response."""
    return b'HTTP/1.1 200 OK\r\n'


def response_error(error_code, error_message):
    """return HTTP server error response."""
    return u'HTTP/1.1 {} {}\r\n\r\n'.format(error_code, error_message).encode('utf-8')


if __name__ == '__main__':
    while True:
        listen_to(server())
