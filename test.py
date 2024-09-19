from app import sumar


def test_sumar():
    assert sumar(1, 2) == 3
    assert sumar(2, 3) == 5