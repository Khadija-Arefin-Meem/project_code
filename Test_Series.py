# testseries.py

import series

def main():
    try:
        n = int(input("Enter a positive integer for the series sum: "))
        if n > 0:
            result = series.sum_series(n)
            print(f"The sum of the series 1 + 2 + 3 + ... + {n} is: {result}")
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
