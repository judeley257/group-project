def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Input from the user
number = int(input("Enter a number (up to 100): "))

print(f"Factorial of {number} is {factorial(number)}")
