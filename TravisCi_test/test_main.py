from main import add

def test_add():
    assert add(2, 3) == 6
    assert add(1, 1) == 2
    assert add(-1, 1) == 0
