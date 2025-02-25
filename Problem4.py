def fizzBuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz") #divisible by 3 and 5
        elif i % 3 == 0:
            result.append("Fizz") #divisible by 3
        elif i % 5 == 0:
            result.append("Buzz")# divisible by 5
        else:
            result.append(str(i))
    return result

n = 5 #how many terms in the list 
output = fizzBuzz(n)
print(output)
