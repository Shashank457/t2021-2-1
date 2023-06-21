class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Cannot divide by zero"


a=float(input("Enter the first number   "))
b=float(input("Enter the second number   "))
calc = Calculator(a, b)
typeOfOperation=input("Enter the type of Operation   ")

if typeOfOperation=="+":
    print("Answer: ",calc.add())
elif typeOfOperation=="-":
    print("Answer: ",calc.subtract())
elif typeOfOperation=="*":
    print("Answer: ",calc.multiply())
elif typeOfOperation=="/":
    print("Answer: ",calc.divide())
else:
    print("Invalid Type of Operation")