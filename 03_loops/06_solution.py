#Problem:compute the factorial of a number using a while loop
number = int(input("please enter a number:"))
factorial = 1

while number > 0:
    #factorial = factorial * number
    #number = number - 1
    factorial *= number
    number -= 1

print("factorial value of a given number is:",factorial)