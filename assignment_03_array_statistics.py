# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================



def calculate_sum(numbers):
    """Calculate all elements in the list using loops"""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Calculate the average of the list"""
    if len(numbers) == 0:
        return 0
    total = calculate_sum(numbers)
    return total / len(numbers)


def find_maximum(numbers):
    """Find the maximum value in the list using loops"""
    max_value = numbers[0]
    for num in numbers[1:]:
        if num > max_value:
            max_value = num
    return max_value


def find_minimum(numbers):
    """Find the minimum value in the list using loops"""
    min_value = numbers[0]
    for num in numbers[1:]:
        if num < min_value:
            min_value = num
    return min_value


def main():
    # Ask the user for the count of numbers
    try:
        n = int(input("How many numbers? "))
    except ValueError:
        print("Error: Please enter a positive integer.")
        return

    if n <= 0:
        print("Error: Please enter a positive integer.")
        return

    numbers = []
    for i in range(n): # fixed: was 'for i in range(n);' with semicolon
        value = float(input(f"Enter number {i+1}: "))
        
        if value.is_integer():
            value = int(value)
        numbers.append(value)

    # calculate results using the functions
    total_sum = calculate_sum(numbers)
    average = calculate_average(numbers) # fixed typo here
    max_value = find_maximum(numbers)
    min_value = find_minimum(numbers)

    # display the results
    print("\nResults:")
    print(f"Sum: {total_sum}")
    print(f"Average: {average}")
    print(f"Maximum: {max_value}")
    print(f"Minimum: {min_value}")


if __name__ == "__main__": # fixed: was __main__
    main()