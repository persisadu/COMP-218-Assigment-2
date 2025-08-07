def hanoi(n, source, target, temp):
    ### Recursive function to solve Tower of Hanoi. Returns a list of move steps in the format: 'source to target'###

    moves = []
    if n == 1:
        # base case: move one disc directly
        moves.append(f"{source} → {target}")
    else:
        # step 1: move n-1 discs from source to temp
        moves += hanoi(n-1, source, temp, target)

        # step 2: move the nth disc from source to target
        moves.append(f"{source} → {target}")

        # step 3: move n-1 discs from temp to target
        moves += hanoi(n-1, temp, target, source)

    return moves


def main():
    n = 3
    moves = hanoi(n, 'A', 'C', 'B')

    for step, move in enumerate(moves, start=1):
        print(f"{step}: {move}")

if __name__ == "__main__":
    main()