# -*- coding: utf-8 -*-
import pytest
import client

BUFFER_LENGTH = 8


def test_short_buff():
    short_buffer = u"word"  # 4 Bytes
    assert client.client(short_buffer) == short_buffer


def test_long_buff():
    test_str = u"a" * 1200
    assert client.client(test_str) == test_str


def test_exact_buff():
    test_str = u"a" * (BUFFER_LENGTH * 3)
    assert client.client(test_str) == test_str


def test_non_ascii():
    test_str = u"Laȝamon was ihoten"
    assert client.client(test_str) == test_str
