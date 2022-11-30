from plates import is_valid


def test_cs50():
    assert is_valid("CS50") == True


def test_cs05():
    assert is_valid("CS05") == False


def test_cs50p():
    assert is_valid("CS50P") == False


def test_pi314():
    assert is_valid("PI3.14") == False


def test_one_letter():
    assert is_valid("H") == False


def test_outatime():
    assert is_valid("OUTATIME") == False
