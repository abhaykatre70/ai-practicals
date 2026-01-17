def construct_odd_magic_grid(size):
    grid_matrix = [[0 for _ in range(size)] for _ in range(size)]

    row_pos = size // 2
    col_pos = size - 1

    current_val = 1
    while current_val <= size * size:
        if row_pos == -1 and col_pos == size:
            row_pos = 0
            col_pos = size - 2

        else:
            if col_pos == size:
                col_pos = 0
            if row_pos < 0:
                row_pos = size - 1

        if grid_matrix[row_pos][col_pos] != 0:
            col_pos -= 2
            row_pos += 1
            continue
        else:
            grid_matrix[row_pos][col_pos] = current_val
            current_val += 1

        col_pos += 1
        row_pos -= 1

    print("\nMagic Square for n =", size)
    print("Sum of each row/column =", size * (size * size + 1) // 2, "\n")

    for grid_row in grid_matrix:
        for cell in grid_row:
            print(f"{cell:2}", end=" ")
        print()


size = int(input("Enter an odd number: "))
construct_odd_magic_grid(size)
