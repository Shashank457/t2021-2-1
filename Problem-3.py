# Problem-3:  With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]

#     Output: (examples)
#         1) input a = 1, then output : 1
#         2) input a = 2, then output : 1
#         3) input a = 3, then output : 1, 3, 5
#         4) input a = 4, then output : 1, 3, 5
#         5) input a = 5, then output : 1, 3, 5, 7, 9
#         6) input a = 6, then output : 1, 3, 5, 7, 9
#         .
#         .
#         7) input a = x, then output : 1, 3, 5, 7, .......








# Created a function to print the answer
def solution(a):
    if a%2 == 0:
        x = 1
        for i in range(a-1):
            print(x,end = "")
            x += 2
            if(i < a-2):
                print(",", end = "")
    else:
        x = 1
        for i in range(a):
            print(x,end = "")
            x += 2
            if(i < a-1):
                print(",", end = "")


inp=int(input("Enter the number   "))
solution(inp)
