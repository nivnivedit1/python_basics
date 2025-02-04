#Basic function syntax
#Problem:write a function to calculate and return the square  of a number
def square_of_num(number):
    print(number ** 2)
result = square_of_num(4)
print(result) 

# bcz result variable ke under value store hi nahi hua ,function ke ander jo 
#print lika hai uski vajah se   alternate solution  in below  code

def square_of_num(number):
    return(number ** 2)
result = square_of_num(4)
print(result)