from day04.main import *
import pytest

def test_can_do_line():
    with open('tests/sample.txt','r') as f:
        lines = f.read().splitlines()
        nums = list(map(int,list(lines.pop(0).split(","))))
        result = puzzle1(lines,nums)
        assert result == 4512

def test_can_parse_boards():
    with open('tests/sample.txt','r') as f:
        lines = f.read().splitlines()
        result = get_boards(lines)
        assert result ==[[[22, 13, 17, 11, 0], [8, 2, 23, 4, 24], [21, 9, 14, 16, 7], [6, 10, 3, 18, 5], [1, 12, 20, 15, 19]], [[3, 15, 0, 2, 22], [9, 18, 13, 17, 5], [19, 8, 7, 25, 23], [20, 11, 10, 24, 4], [14, 21, 16, 12, 6]], [[14, 21, 17, 24, 4], [10, 16, 15, 9, 19], [18, 8, 23, 26, 20], [22, 11, 13, 6, 5], [2, 0, 12, 3, 7]]] 

def test_can_check_boards():
    with open('tests/sample.txt','r') as f:
        lines = f.read().splitlines()
        nums = list(map(int,list(lines.pop(0).split(","))))
        boards = get_boards(lines)
        result = check_boards(boards,nums,[])
        assert result == 4512

def test_can_let_the_squid_win():
    with open('tests/sample.txt','r') as f:
        lines = f.read().splitlines()
        nums = list(map(int,list(lines.pop(0).split(","))))
        result = puzzle2(lines,nums) 
        assert result == 1924
