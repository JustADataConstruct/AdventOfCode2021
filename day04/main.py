def puzzle1(lines,nums) -> int:
    boards = get_boards(lines)
    result = check_boards(boards,nums,[])
    return result

def get_boards(lines):
    boards = []
    for i, l in enumerate(lines):
        if l == "":
            board = []
            for x in range(i+1,i+6):
                b = lines[x].split(" ")
                nums = list(map(int,[a for a in b if a]))
                board.append(nums)
            boards.append(board)
    return boards

def check_boards(boards, nums, solved):
    length = len(boards[0][0])
    for num in nums:
        for board in boards:
            for line in board:
                if num in line:
                    line[line.index(num)] = 0
                if line == [0,0,0,0,0]:
                    boards.pop(boards.index(board))
                    result = sum([sum(line) for line in board]) * num 
                    solved.append(result)
                    return result
            for i in range(0,length-1):
                pos = [line[i] for line in board]
                if pos == [0,0,0,0,0]:
                    boards.pop(boards.index(board))
                    result = sum([sum(line) for line in board]) * num 
                    solved.append(result)
                    return result
    return -1

def puzzle2(lines,nums):
    boards = get_boards(lines)
    amount = len(boards)
    solved = []
    while len(solved)  < amount:
        check_boards(boards,nums,solved)
    return solved[-1]

if __name__ == "__main__":
    with open('input.txt','r') as f:
        lines = f.read().splitlines()
    nums = list(map(int,list(lines.pop(0).split(","))))
    print(f"Puzzle 1: {puzzle1(lines,nums)}")
    print(f"Puzzle 2: {puzzle2(lines,nums)}")
