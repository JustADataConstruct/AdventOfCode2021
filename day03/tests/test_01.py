from day03.main import *
def test_get_power_consumption():
    with open('tests/sample.txt','r') as f:
        lines = f.readlines()
        result = puzzle1(lines)
        assert result == 198

def test_oxygen_generator_rating():
    with open('tests/sample.txt','r') as f:
        lines = f.readlines()
        result = calculate_oxygen_generator_rating(lines) 
        assert result == 23

def test_co2_scrubber_rating():
    with open('tests/sample.txt','r') as f:
        lines = f.readlines()
        result = calculate_co2_scrubber_rating(lines) 
        assert result == 10

def test_life_support_rating():
    with open('tests/sample.txt','r') as f:
        lines = f.readlines()
        result = puzzle2(lines) 
        assert result == 230
