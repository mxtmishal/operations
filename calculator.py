class calculator:
    def add(self,a,b):
        return a + b
    def subtract(self,a,b):
        return a - b
    def multiply(self,a,b):
        return a * b
    def divide(self,a,b):
        if b == 0:
            return a / b
calc = calculator()

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

print("1.Add")
print("2.Subtract")     
print("3.Multiply")     
print("4.Devide")     
    
     
choice = int(input("choose operation (1-4): "))

if choice == 1:
    print("Result:",calc.add(a,b))
elif choice == 2:
    print("Result:",calc.subtract(a,b))
elif choice == 3:
    print("Result:",calc.multiply(a,b))
elif choice == 4:
    print("Result:",calc.divide(a,b))
else:
    print("Invalid choice")
    
