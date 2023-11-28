# This function checks if exactly two out of three given numbers are positive.

def check_params_contain_two_positive_numbers(a, b, c):
    # Initialize a variable to count the number of positive numbers.
    num = 0

    # Check if the first parameter 'a' is positive.
    if a > 0:
        num += 1

    # Check if the second parameter 'b' is positive.
    if b > 0:
        num += 1

    # Check if the third parameter 'c' is positive.
    if c > 0:
        num += 1

    # If exactly two out of three numbers are positive, return True.
    if num == 2:
        return True

    # If the condition is not met, return False.
    return False
