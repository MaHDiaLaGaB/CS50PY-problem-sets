from fuel import gauge, convert
import pytest

def test_gauge_one():
    assert convert('3/4') == 75
    assert gauge(75) == '75%'

def test_gauge_two():
    assert convert('1/4') == 25
    assert gauge(25) == '25%'

def test_gauge_three():
    assert convert('4/4') == 100
    assert gauge(100) == 'F'
    assert gauge(99) == 'F'

def test_gauge_four():
    assert convert('0/4') == 0
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_value_error():
    with pytest.raises(ValueError):
        convert('cat/1')


