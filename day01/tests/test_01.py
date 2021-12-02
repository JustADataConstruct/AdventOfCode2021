from day01.main import *
def test_count_number_times():
    with open('tests/sample_01.txt','r') as f:
        lines = f.readlines()
        result = puzzle1(lines)
        assert result == 7
def test_larger_sums():
    with open('tests/sample_01.txt','r') as f:
        lines = f.readlines()
        result = puzzle2(lines) 
        assert result == 5
