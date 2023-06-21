# Problem-4:  Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
#     (examples)
#     input: [1,2,8,9,12,46,76,82,15,20,30]
#     Output:
#         {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}







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
