import random

def display_grid(grid):
    print("-------------")
    for r in range(3):
        print("|", end=" ")
        for c in range(3):
            print(grid[r][c], end=" | ")
        print("\n-------------")

def has_winner(grid, symbol):
    for r in range(3):
        if grid[r][0] == grid[r][1] == grid[r][2] == symbol:
            return True

    for c in range(3):
        if grid[0][c] == grid[1][c] == grid[2][c] == symbol:
            return True

    if grid[0][0] == grid[1][1] == grid[2][2] == symbol:
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] == symbol:
        return True

    return False

def ai_turn(grid):
    for r in range(3):
        for c in range(3):
            if grid[r][c] == " ":
                grid[r][c] = "O"
                if has_winner(grid, "O"):
                    return

                grid[r][c] = " "

    for r in range(3):
        for c in range(3):
            if grid[r][c] == " ":
                grid[r][c] = "X"
                if has_winner(grid, "X"):
                    grid[r][c] = "O"
                    return

                grid[r][c] = " "

    while True:
        r = random.randint(0, 2)
        c = random.randint(0, 2)
        if grid[r][c] == " ":
            grid[r][c] = "O"
            return

def start_match():
    grid = [[" " for _ in range(3)] for _ in range(3)]

    active_symbol = "X"

    while True:
        display_grid(grid)

        if active_symbol == "X":
            while True:
                r_pos = int(input("Enter the row (0-2): "))
                c_pos = int(input("Enter the column (0-2): "))
                if grid[r_pos][c_pos] == " ":
                    grid[r_pos][c_pos] = "X"
                    break
                else:
                    print("Invalid move. Try again.")
        else:
            ai_turn(grid)

        if has_winner(grid, active_symbol):
            display_grid(grid)
            print(f"{active_symbol} wins!")
            break

        if all(grid[r][c] != " " for r in range(3) for c in range(3)):
            display_grid(grid)
            print("It's a draw")
            break

        active_symbol = "O" if active_symbol == "X" else "X"

start_match()