import random

inputNumber = eval(input("Enter the number: "))

winningNumber = random.randint(10,99)
print("Winning Number is", winningNumber)
num1 = winningNumber // 10
num2 = winningNumber % 10

if num1 == inputNumber // 1 and num2 == inputNumber % 10 :
    print("Excellent!!! : you win $100,000")
elif num1 == inputNumber % 10 and num2 == inputNumber // 10:
    print("very good : you win $30,000")
elif num1 == inputNumber % 10 or \
        num1 == inputNumber // 10 or \
        num2 == inputNumber % 10 or \
        num2 == inputNumber // 10 :
    print("$1,000")
else :
    print("nt")
