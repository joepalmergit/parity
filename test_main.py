from main import parity

def test_odd_numbers():
    assert parity(1) == 'Odd'
    assert parity(3) == 'Odd'
    assert parity(5) == 'Odd'


def test_even_numbers():
    assert parity(2) == 'Even'
    assert parity(4) == 'Even'
    assert parity(6) == 'Even'
