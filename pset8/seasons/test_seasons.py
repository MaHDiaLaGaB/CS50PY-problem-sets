from seasons import convert
import pytest

def test_convert():
    assert convert('2021-08-12') == 'Seven hundred seventeen thousand, one hundred twenty minutes'
    assert convert('2020-08-12') == 'One million, two hundred forty-two thousand, seven hundred twenty minutes'

def test_error():
    with pytest.raises(SystemExit):
        convert('2020-8-12')