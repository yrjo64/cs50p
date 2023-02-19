import pytest

from working import convert


def test_no_zeros():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_zeros():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_no_pmam():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_over_minutes():
    with pytest.raises(Exception):
        convert("9:60 AM to 5:60 PM")


def test_no_to():
    with pytest.raises(Exception):
        convert("9:00 AM - 5:00 PM")


def test_no_wrong1():
    with pytest.raises(Exception):
        convert("09:00 AM to 17:00 PM")

def test_no_wrong2():
    with pytest.raises(Exception):
        convert("09:00 to 11:00")
