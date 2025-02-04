# problem:reverse a string using a loop

input_str = input("Please provide me a string:")
reversed_str = ""


for str in input_str:
    reversed_str = str + reversed_str
    print(str)

print(reversed_str)
 