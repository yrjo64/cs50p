import pytest

from numb3rs import validate


def test_ok():
    assert validate("1.1.1.1")


def test_not_ok():
    assert not validate("1.265.1.1")


def test_too_few_params():
    assert not validate("1.1.1")


def test_not_comma():
    assert not validate("1.1.1,1")


def test_something_else():
    assert not validate("cat")
