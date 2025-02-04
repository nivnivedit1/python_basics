# problem:calculate the sum of even numbers upto a given number n.
n = int(input("provide a number range:"))
sum_even = 0

for i in range(1,n+1):
    if i%2 == 0:
        sum_even +=1
print("the sum of even number is:",sum_even)