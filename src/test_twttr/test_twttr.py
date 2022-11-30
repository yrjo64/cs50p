from twttr import shorten


def test_default():
    assert shorten("hello") == "hll"
    assert shorten("Hello world1") == "Hll wrld1"
    assert shorten("hello world") == "hll wrld"


def test_no_vowels():
    assert shorten("kkk") == "kkk"


def test_capital_vowel():
    assert shorten("nO") == "n"


def test_s1():
    assert shorten("What's your name?") == "Wht's yr nm?"


def test_fails():
    assert shorten("HELLO WORLD") != "HeLLo WoRLD"


# def test_null():
#    assert shorten(None) is None


def test_empty():
    assert shorten("") == ""
