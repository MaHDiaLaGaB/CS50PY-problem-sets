from twttr import shorten

def test_shorten():
    short = shorten("hello, world")
    assert short == "hll, wrld"

def test_long_text():
    long = shorten("fAcebook is really bad platform")
    assert long == "fcbk s rlly bd pltfrm"

def test_omitting_num():
    num = shorten("here there is 2022")
    assert num == "hr thr s 2022"