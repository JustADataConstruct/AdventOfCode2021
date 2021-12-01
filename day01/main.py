def puzzle1(lines):
    count= 0
    for i in range(1,len(lines)):
        if int(lines[i]) > int(lines[i-1]):
           count += 1 
    return count

def puzzle2(lines):
    count = 0
    last = sum(map(int,lines[0:3]))
    for i in range(0,len(lines)):
        if i+3 > len(lines):
            break
        this = sum(map(int,lines[i:i+3])) 
        if this > last:
            count += 1
        last = this
    return count 

if __name__ == "__main__":
    with open('input.txt','r') as f:
        lines = f.readlines()
    print(f"Puzzle 1: {puzzle1(lines)}")
    print(f"Puzzle 2: {puzzle2(lines)}")
