# -*- coding: utf-8 -*-
import pytest
import client
import server

def test_response_ok():
    assert server.response_ok() == b'HTTP/1.1 200 OK\r\n\r\n'


def test_HTTP_response():
    assert len(client.client(u"Some Message").splitlines()) == 2