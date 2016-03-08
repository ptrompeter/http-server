import pytest
import server
import client

BUFFER_LENGTH = 8


def test_short_buff():
    short_buffer = u"word"  # 4 Bytes
    assert client.client(short_buffer) == short_buffer


def test_long_buff():
    test_str = u"a" * (BUFFER_LENGTH * 10)
    assert client.client(test_str) == test_str


def test_exact_buff():
    test_str = u"Good day"  # 8 bytes
    assert client.client(test_str) == test_str


def test_non_ascii():
    test_str = u"ƒåncy ¥o"
    assert client.client(test_str) == test_str
