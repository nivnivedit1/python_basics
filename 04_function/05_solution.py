#Default parameter value
#Problem:write a function that greets a user .if no name is provided,it should greet with a default name.
def greet(name="kitty"):
    return ("Hello,"+ name + "!")
print(greet())
print(greet("chai"))