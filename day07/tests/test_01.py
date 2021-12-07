from day07.main import *
import pytest

def test_01():
    with open('tests/sample.txt','r') as f:
        lines = f.read().split(",")
        result = puzzle1(lines)
        assert result == 37

@pytest.mark.skip(reason="Not reached")
def test_02():
    with open('tests/sample.txt','r') as f:
        lines = f.read().split(",")
        result = puzzle2(lines) 
        assert result == 168
