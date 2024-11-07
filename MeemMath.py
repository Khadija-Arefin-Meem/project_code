from mpmath import mp

def printBigpi(n):
    mp.dps = n + 1  # Set decimal places to n + 1
    return str(mp.pi)  # Return pi with the specified precision

# Example usage
print(printBigpi(10))  # Will print pi to 10 decimal places
