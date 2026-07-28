# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_fibonacci(n):
    """
    Generates and prints the first N terms of the Fibonacci sequence.
    """
    if n <= 0:
        print("Error: Please enter a positive integer.")
        return

    sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    # Print numbers joined by a single space
    print("Fibonacci sequence:", " ".join(str(num) for num in sequence))


def is_fibonacci(num):
    """
    Checks whether a given non-negative integer belongs to the Fibonacci sequence.
    Returns True if it is a Fibonacci number, False otherwise.
    """
    if num < 0:
        return False

    a, b = 0, 1
    
    # Loop and generate terms until we reach or exceed the target number
    while a < num:
        a, b = b, a + b

    return a == num


def main():
    # -------------------------------------------------------------------------
    # PART A — Print the First N Terms
    # -------------------------------------------------------------------------
    try:
        n_terms = int(input("How many terms? "))
        print_fibonacci(n_terms)
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    print()  # Blank line for clean spacing

    # -------------------------------------------------------------------------
    # PART B — Check if a Number Belongs to the Sequence
    # -------------------------------------------------------------------------
    try:
        check_num = int(input("Enter a number to check: "))
        if is_fibonacci(check_num):
            print(f"{check_num} is a Fibonacci number.")
        else:
            print(f"{check_num} is NOT a Fibonacci number.")
    except ValueError:
        print("Error: Please enter a valid integer.")


if __name__ == "__main__":
    main()