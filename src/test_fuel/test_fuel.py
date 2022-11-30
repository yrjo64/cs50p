from fuel import gauge, convert
import pytest


def test_convert_lt_1():
    assert convert("56/9789") == 1.0


def test_convert_gt_99():
    assert convert("100 / 101") == 99.00


def test_convert_gt_ab():
    with pytest.raises(Exception):
        convert("1000 / 101")


def test_convert_zero():
    with pytest.raises(Exception):
        convert("1000 / 0")


def test_gauge_1():
    assert gauge(1) == "E"


def test_gauge_0():
    assert gauge(0) == "E"


def test_gauge_56():
    assert gauge(56) == "56%"


def test_gauge_99():
    assert gauge(99) == "F"


def test_gauge_95():
    assert gauge(95) == "95%"
