from src.main import add, subtract

def test_add_funcation():
    assert add(5, 3) == 8
    assert add(6, 4) == 10
    assert add(5, 4) == 9

def test_subtract_funcation():
    assert subtract(5, 3) == 2
    assert subtract(6, 4) == 2
    assert subtract(5, 4) == 1





