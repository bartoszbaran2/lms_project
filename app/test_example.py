from decimal import Decimal

import pytest


def divide(a, b):  # nie ma wyjatku to if
    if not isinstance(a, (int, float)) or not isinstance(b,(int, float)):
        raise TypeError(f'Invalid input {a}, {b}.')
    return a / b


def test_correct_result():
    assert divide(10, 5) == 2


def test_incorrect_input_type():
    with pytest.raises(TypeError) as excinfo:
        divide('1', '2')
    assert 'Invalid input' in str(excinfo.value)


def test_input_decimal():
    with pytest.raises(TypeError) as excinfo:
        divide(Decimal('1'), '2')
    assert 'Invalid input' in str(excinfo.value)


def test_zero_dividing():
    with pytest.raises(ZeroDivisionError) as excinfo:
        divide(10, 0)
    assert 'division by zero' in str(excinfo.value)


'''
try: # kazdy blok test case
    divide(2, 0)
    print('test failed')
except ZeroDivisionError:
    print('.')
'''