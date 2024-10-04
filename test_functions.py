import pytest
from example_functions import my_adder, my_thermo_stat, have_digits

@pytest.mark.parametrize("a, b, c, expected_sum", [
    (1, 2, 3, 6), (-1, 2, 3, 4), (0, 0, 0, 0), (0, -1, 1, 0), (1.5, 2.5, 3.0, 7.0)
])
def test_my_adder(a, b, c, expected_sum):
    output = my_adder(a, b, c)
    assert output == expected_sum

@pytest.mark.parametrize("temp, desired_temp, expected_status", [
    (60, 70, 'Heat'),
    (80, 70, 'AC'),
    (67, 70, 'off'),
    (65, 70, 'off'),
    (75, 70, 'off'),
])
def test_my_thermo_stat(temp, desired_temp, expected_status):
    output = my_thermo_stat(temp, desired_temp)
    assert output == expected_status

@pytest.mark.parametrize("s, expected_output", [
    ("hello123", 1),
    ("abc", 0),
    ("123", 1),
    ("", 0),
    ("hello world!", 0),
    ("test2021", 1),
    ("$%#@", 0),
    ("4you", 1)
])
def test_have_digits(s, expected_output):
    output = have_digits(s)
    assert output == expected_output