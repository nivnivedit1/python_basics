x = 99
def func2(y):
    z = x + y  # it taking x value from global scope
    return z
result = func2(1)
print(result)
# dont override global values  like shown in below code 
#its not good dont override like this below code
x = 99
def func3():
    global x
    x = 12
func3()
print(x)
# first it sees in local scope if it has x ok or it print the x which has in global scope
def f1():
    x = 88
    def f2():
        print(x)
    f2()
f1()

#factory function or closure 
def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))