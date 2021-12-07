#TODO: Optimize
def puzzle1(values,days) -> int:
    state = list(map(int,values))
    for i in range(0,days):
        for fish in range(0,len(state)):
            if state[fish] == 0:
                state.append(8)
                state[fish] = 7
            state[fish] -= 1
    return len(state)

if __name__ == "__main__":
    with open('input.txt','r') as f:
        input = f.read().rstrip()
        values = input.split(",")
    print(f"Puzzle 1: {puzzle1(values,80)}")
#    print(f"Puzzle 2: {puzzle1(values,256)}")
