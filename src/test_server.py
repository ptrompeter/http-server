# -*- coding: utf-8 -*-
import pytest
import client
import server

USR_MESSAGES = [
    b'GET sumjunkz HTTP/1.1\r\nHost:adfisojasdfiidfs\r\nDate:aifsuhdskdfhsdg\r\n\r\nasdfiojasdfjiopasdfpijo',
    b'POST sumjunkz HTTP/1.1\r\nHost:asdfasdfasdf\r\n\r\n',
    b'GET sumjunkz HTTP/1.0\r\nHost:asdfasdfg\r\n\r\n',
    b'GET sumjunkz HTTP/1.1\r\nDate:ioersjfisogio\r\n\r\n'
]

def test_response_ok():
    assert server.response_ok() == b'HTTP/1.1 200 OK\r\n\r\n'


def test_HTTP_response():
    assert len(client.client(u"Some Message").splitlines()) == 2

#@pytest.mark.parametrize('a', USR_MESSAGES)
def test_parse_good():
    assert server.parse_request(USR_MESSAGES[0]) == b'sumjunkz'

def test_parse_post():
    with pytest.raises(AttributeError):
        server.parse_request(USR_MESSAGES[1])

def test_parse_http():
    with pytest.raises(EnvironmentError):
        server.parse_request(USR_MESSAGES[2])

def test_parse_host():
    with pytest.raises(NameError):
        server.parse_request(USR_MESSAGES[3])
