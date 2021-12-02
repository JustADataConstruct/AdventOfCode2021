from day02.main import *
def test_can_parse_and_multiply():
    with open('tests/sample.txt','r') as f:
        lines = f.readlines()
        result = puzzle1(lines)
        assert result == 150

def test_can_handle_aim():
    with open('tests/sample.txt','r') as f:
        lines = f.readlines()
        result = puzzle2(lines) 
        assert result == 900
