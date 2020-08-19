# Given an integer, n, print the following values for each integer i from 1 to n:
# 1. Decimal
# 2. Octal
# 3. Hexadecimal (capitalized)
# 4. Binary
# The four values must be printed on a single line in the order specified above for each i from 1 to n.
# Each value should be space-padded to match the width of the binary value of n.

# Input Format
# A single integer denoting n.

# Constraints
# 1 ≤ n ≤ 99

# Output Format
# Print n lines where each line i (in the range 1 ≤ i ≤ n) contains the respective decimal, octal, capitalized hexadecimal, and binary values of i. Each printed value must be formatted to the width of the binary value of n.

def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        print(' '.join(map(lambda x: x.rjust(width), [str(i), oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:]])))