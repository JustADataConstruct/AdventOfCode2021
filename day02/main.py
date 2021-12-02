def puzzle1(lines) -> int:
    hor = 0
    ver = 0
    for i in lines:
        dir = i.split(" ")[0]
        amount = int(i.split(" ")[1])
        if dir == "forward":
            hor += amount
        elif dir == "down":
            ver += amount
        elif dir == "up":
            ver -= amount
    return hor * ver


def puzzle2(lines):
    hor = 0
    ver = 0
    aim = 0
    for i in lines:
        dir = i.split(" ")[0]
        amount = int(i.split(" ")[1])
        if dir == "forward":
            hor += amount
            ver += aim*amount
        elif dir == "down":
            aim += amount
        elif dir == "up":
            aim -= amount
    return hor * ver

if __name__ == "__main__":
    with open('input.txt','r') as f:
        lines = f.readlines()
    print(f"Puzzle 1: {puzzle1(lines)}")
    print(f"Puzzle 2: {puzzle2(lines)}")
