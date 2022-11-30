import bank


def test_hello():
    assert bank.value("hello friend") == 0


def test_hello_upper():
    assert bank.value("Hello friend") == 0


def test_starts_h():
    assert bank.value("how do you do friend?") == 20


def test_starts_H():
    assert bank.value("How do you do friend?") == 20


def test_hundred():
    assert bank.value("Nice day to day, isn't it?") == 100
