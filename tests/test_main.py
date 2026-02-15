from src.main import add

def test_add_funcation():
    assert add(5, 3) == 8
    assert add(6, 4) == 10
    assert add(5, 4) == 10


