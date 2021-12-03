from collections import Counter

def puzzle1(lines) -> int:
    gamma = ""
    epsilon = ""
    length = len(lines[0])
    for pos in range(0,length-1):
        chars = [x[pos] for x in lines]
        counter = Counter(chars)
        gamma += counter.most_common()[0][0]
        epsilon += counter.most_common()[-1][0]
    return int(gamma,2) * int(epsilon,2)

def puzzle2(lines):
    oxygen = calculate_oxygen_generator_rating(lines)
    co2 = calculate_co2_scrubber_rating(lines)
    return oxygen * co2

def calculate_oxygen_generator_rating(lines) -> int:
    length = len(lines[0])
    for pos in range(0,length-1):
        if len(lines) == 1:
            break
        counter = Counter([x[pos] for x in lines])
        num = counter.most_common()[0][0] if counter.most_common()[0][1] != counter.most_common()[1][1] else '1' 
        lines = [l for l in lines if l[pos] == num]
    return int(lines[-1],2)

def calculate_co2_scrubber_rating(lines) -> int:
    length = len(lines[0])
    for pos in range(0,length-1):
        if len(lines) == 1:
            break
        counter = Counter([x[pos] for x in lines])
        num = counter.most_common()[-1][0] if counter.most_common()[-1][1] != counter.most_common()[0][1] else '0' 
        lines = [l for l in lines if l[pos] == num]
    return int(lines[-1],2)


if __name__ == "__main__":
    with open('input.txt','r') as f:
        lines = f.readlines()
    print(f"Puzzle 1: {puzzle1(lines)}")
    print(f"Puzzle 2: {puzzle2(lines)}")
