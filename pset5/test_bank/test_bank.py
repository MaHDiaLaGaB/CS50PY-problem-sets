from bank import value


def test_value():
    assert value("hello") == 0
    assert value("How") == 20
    assert value("watsup") == 100


# def test_faild_value():
#     assert value('up') == 20