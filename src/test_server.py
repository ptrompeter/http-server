# -*- coding: utf-8 -*-
import pytest
import client
import server


CONTENT_TYPES = [
b'Content-Type: text/plain',
b'Content-Type: image/jpeg',
b'Content-Type: image/png',
b'Content-Type: text/html',
b'Content-Type: text/python',
]


USR_MESSAGES = [
    b'GET /sample.txt HTTP/1.1\r\nHost:adfisojasdfiidfs\r\nDate:aifsuhdskdfhsdg\r\n\r\n\r\n',
    b'POST sumjunkz HTTP/1.1\r\nHost:asdfasdfasdf\r\n\r\n',
    b'GET sumjunkz HTTP/1.0\r\nHost:asdfasdfg\r\n\r\n',
    b'GET sumjunkz HTTP/1.1\r\nDate:ioersjfisogio\r\n\r\n'
]


def test_response_ok():
    assert server.response_ok() == b'HTTP/1.1 200 OK\r\n'


def test_HTTP_response():
    assert client.client(USR_MESSAGES[0]) == u'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nThis is a very simple text file.\nJust to show that we can serve it up.\nIt is three lines long.\n\r\n\r\n'
    #assert client.client(USR_MESSAGES[1]) == u'HTTP/1.1 405 Method Not Allowed\r\n\r\n'
    #assert client.client(USR_MESSAGES[2]) == u'HTTP/1.1 406 Not Acceptable\r\n\r\n'
    #assert client.client(USR_MESSAGES[3]) == u'HTTP/1.1 400 Bad Request\r\n\r\n'

#@pytest.mark.parametrize('a', USR_MESSAGES)
def test_parse_good():
    assert server.parse_request(USR_MESSAGES[0]) == b'/sample.txt'


def test_parse_post():
    with pytest.raises(AttributeError):
        server.parse_request(USR_MESSAGES[1])


def test_parse_http():
    with pytest.raises(TypeError):
        server.parse_request(USR_MESSAGES[2])


def test_parse_host():
    with pytest.raises(NameError):
        server.parse_request(USR_MESSAGES[3])


def test_resolve_uri_txt():
    assert server.resolve_uri(b'/sample.txt')[1] == CONTENT_TYPES[0]


def test_resolve_uri_jpeg():
    assert server.resolve_uri(b'/images/JPEG_example.jpg')[1] == CONTENT_TYPES[1]


def test_resolve_uri_png():
    assert server.resolve_uri(b'/images/sample_1.png')[1] == CONTENT_TYPES[2]


def test_resolve_uri_html():
    assert server.resolve_uri(b'/a_web_page.html')[1] == CONTENT_TYPES[3]


def test_resolve_uri_python():
    assert server.resolve_uri(b'/make_time.py')[1] == CONTENT_TYPES[4]


def test_resolve_uri_directory():
    assert server.resolve_uri(b'/images')[1] == CONTENT_TYPES[3]


def test_resolve_uri_bad():
    with pytest.raises(IOError):
        server.resolve_uri(b'/badfile.txt')


def test_html_maker():
    test_response = b'<!DOCTYPE html><html><body><a href="/images/JPEG_example.jpg">JPEG_example.jpg</a><a href="/images/sample_1.png">sample_1.png</a><a href="/images/Sample_Scene_Balls.jpg">Sample_Scene_Balls.jpg</a></body></html>'
    assert server.html_maker('webroot/images', b'/images') == test_response

