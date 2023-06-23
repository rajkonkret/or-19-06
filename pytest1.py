import pytest


def calculate_square(num):
    return num ** 2


@pytest.mark.parametrize("input, expected_output", [(2, 4), (3, 9), (4, 16)])
def test_square_calculation(input, expected_output):
    assert calculate_square(input) == expected_output
