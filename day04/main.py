def puzzle1(lines) -> int:
    nums = list(map(int,list(lines.pop(0).split(","))))
    boards = get_boards(lines)
    result = check_boards(boards,nums)
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

def check_boards(boards, nums):
    length = len(boards[0][0])
    for num in nums:
        for board in boards:
            for line in board:
                if num in line:
                    line[line.index(num)] = 0
                if line == [0,0,0,0,0]:
                    result = sum([sum(line) for line in board]) * num 
                    return result
            for i in range(0,length-1):
                pos = [line[i] for line in board]
                if pos == [0,0,0,0,0]:
                    result = sum([sum(line) for line in board]) * num 
                    return result
    return -1

def puzzle2(lines):
    return 0

if __name__ == "__main__":
    with open('input.txt','r') as f:
        lines = f.read().splitlines()
    print(f"Puzzle 1: {puzzle1(lines)}")
    print(f"Puzzle 2: {puzzle2(lines)}")
