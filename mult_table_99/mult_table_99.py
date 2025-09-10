# -*- coding: UTF-8 -*-

# Beginner Version: Standard 9×9 (triangle style)
def mult_table_9x9():
    for i in range(1, 10):# Rows: 1 to 9
        for j in range(1, i+1): # Columns: 1 to current row
            print(f"{j}x{i}={i*j}", end="\t")
        print()


# Advanced Version: Custom Range & Style
def print_mult_table(n=9, triangular=True):
    """
    n: maximum multiplier, e.g. 9 means 1~9
    triangular: True = lower-triangle table, False = full square table
    """
    # Calculate cell width so the table looks aligned
    cell_w = len(str(n)) * 2 + len(str(n*n)) + 3

    for i in range(1, n + 1):
        for j in range(1, (i + 1) if triangular else (n + 1)):
            text = f"{j}×{i}={i * j}"
            print(text.ljust(cell_w), end="")
        print()


if __name__ == '__main__':
    mult_table_9x9()

    print("")

    print("=== 9×9 Triangle Table ===")
    print_mult_table(9, triangular=True)

    print("")

    print("\n=== 12×12 Full Square Table ===")
    print_mult_table(12, triangular=False)
