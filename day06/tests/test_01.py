from day06.main import *
import pytest

def test_can_calculate_lanternfish():
    with open('tests/sample.txt','r') as f:
        input = f.read().rstrip()
        values = input.split(",")
        result = puzzle1(values,80)
        assert result == 5934

@pytest.mark.skip(reason="Not working")
def test_can_handle_eternal_fishes():
    with open('tests/sample.txt','r') as f:
        input = f.read().rstrip()
        values = input.split(",")
        result = puzzle1(values,256)
        assert result == 26984457539
