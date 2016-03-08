import pytest
import server
import client

BUFFER_LENGTH = 1024

def test_short_buff():
    short_buffer = u"this is my test message."  # 24 Bytes
    assert client.client(short_buffer) == short_buffer
