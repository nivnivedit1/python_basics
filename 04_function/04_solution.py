#function returning multiple values
#Problem:Create a function that returns both the area and circumference of a circle given  its radius
import math

def circle_stats(radius):
    area = format(math.pi * radius ** 2,".2f")
    circumference = round(2 * math.pi * radius)
    return area,circumference
a,c = circle_stats(3) 
print("Area:",a,"circumference:", c)