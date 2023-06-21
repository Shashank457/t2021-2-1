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
