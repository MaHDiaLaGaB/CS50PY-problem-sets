from numb3rs import validate

valid_ip = "255.255.255.255"
not_valid = "512.512.512.512"
def test_isvalid():
    assert validate('255.255.255.255') == True
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
    assert validate('1.555.256.277') == False
    assert validate('cat') == False