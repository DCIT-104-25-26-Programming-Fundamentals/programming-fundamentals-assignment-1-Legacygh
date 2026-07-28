
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def read_matrix(rows, cols, name=""):
    prefix = f"for Matrix {name}" if name else ""
    print(f"\nEnter elements {prefix} ({rows} x {cols}):")
    matrix = []
    for i in range(rows):
        while True:
            row_str = input(f"Enter row {i + 1}: ").strip()
            row_values = list(map(int, row_str.split()))
            if len(row_values) == cols:
                matrix.append(row_values)
                break
            else:
                print(f"Error: Expected {cols} values, but got {len(row_values)}. Try again.")
    return matrix

def print_matrix(matrix, title="Matrix"):
    print(f"\n--- {title} ---")
    if not matrix:
        print("Empty Matrix")
        return
    for row in matrix:
        formatted_row = " ".join(f"{val:5d}" for val in row)
        print(formatted_row)

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)
    return transposed

def add_matrices(a, b):
    rows = len(a)
    cols = len(a[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result

def multiply_matrices(a, b):
    m = len(a)
    n = len(a[0])
    p = len(b[0])
    result = []
    for i in range(m):
        row = []
        for j in range(p):
            total = 0
            for k in range(n):
                total += a[i][k] * b[k][j]
            row.append(total)
        result.append(row)
    return result

def run_part_a():
    print("\n" + "=" * 40)
    print("PART A: Matrix Transpose")
    print("=" * 40)
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)
    print_matrix(matrix, "Original Matrix")
    print_matrix(transpose_matrix(matrix), "Transposed Matrix")

def run_part_b():
    print("\n" + "=" * 40)
    print("PART B: Add Two Matrices")
    print("=" * 40)
    rows = int(input("Enter rows: "))
    cols = int(input("Enter columns: "))
    a = read_matrix(rows, cols, name="A")
    b = read_matrix(rows, cols, name="B")
    print_matrix(a, "Matrix A")
    print_matrix(b, "Matrix B")
    print_matrix(add_matrices(a, b), "Sum (A + B)")

def run_part_c():
    print("\n" + "=" * 40)
    print("PART C: Multiply Two Matrices")
    print("=" * 40)
    m = int(input("Enter rows for A: "))
    n = int(input("Enter cols for A / rows for B: "))
    p = int(input("Enter cols for B: "))
    a = read_matrix(m, n, name="A")
    b = read_matrix(n, p, name="B")
    print_matrix(a, "Matrix A")
    print_matrix(b, "Matrix B")
    print_matrix(multiply_matrices(a, b), "Product (A x B)")

def main():
    while True:
        print("\n" + "=" * 40)
        print(" MATRIX OPERATIONS PROGRAM ")
        print("=" * 40)
        print("1. Part A: Transpose Matrix")
        print("2. Part B: Add Two Matrices")
        print("3. Part C: Multiply Two Matrices")
        print("4. Run All Parts")
        print("5. Exit")
        choice = input("\nSelect an option (1-5): ").strip()
        if choice == "1":
            run_part_a()
        elif choice == "2":
            run_part_b()
        elif choice == "3":
            run_part_c()
        elif choice == "4":
            run_part_a()
            run_part_b()
            run_part_c()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1-5.")

if __name__ == "__main__":
    main()