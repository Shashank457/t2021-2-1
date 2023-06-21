inp = input("Enter the numbers ").split(" ")
numbers = [int(i) for i in inp]
factors = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = {}

# Initialize counts for each factor to 0
for factor in factors:
    result[factor] = 0

# Iterate over the numbers and count the multiples
for number in numbers:
    for factor in factors:
        if number % factor == 0:
            result[factor] += 1
print(result)
