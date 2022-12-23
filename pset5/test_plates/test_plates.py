from plates import is_valid

def test_is_valid_all():
    assert is_valid("CS50") == True

def test_is_valid_one():
    assert is_valid("509832") == False

def test_is_valid_two():
    assert is_valid("CS500P") == False

def test_is_valid_tree():
    assert is_valid("OUTATIME") == False

def test_is_valid_four():
    assert is_valid("GOG050") == False

def test_is_valid_five():
    assert is_valid("PI3.14") == False



