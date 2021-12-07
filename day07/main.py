import statistics

def puzzle1(lines) -> int:
    numbers = list(map(int,[a.rstrip() for a in lines]))
    md = statistics.median(numbers)
    fuel = 0
    for i in numbers:
        fuel += int(max(i,md) - min(i,md))
    return fuel

def puzzle2(lines):
    return -1


if __name__ == "__main__":
    with open('input.txt','r') as f:
        lines = f.read().split(",")
    print(f"Puzzle 1: {puzzle1(lines)}")
    print(f"Puzzle 2: {puzzle2(lines)}")
