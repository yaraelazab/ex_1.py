"""
 problem_0 is add two numbers then out sum of them :
 input = num1 , num2
 output = sum
"""
# soluation_1
num1 = int(input("Number 1 = "))
num2 = int(input("Number 2 = "))
print(f"Sum = {num1 + num2}")

#solution_2 in function
def add(x,y):
    return  x + y

num1 = input("Frist Number : ")
num2 = input("Second Number : ")
# transfer string to int
num1 = int(num1)
num2 = int(num2)
print(f"Sum of {num1} and {num2} is {add(num1,num2)}")