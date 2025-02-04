#function with kwargs
#Problem:Create a function that accepts any number of keyword arguments and prints them in the format key:value.
def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_kwargs(name="nivi",state="karnataka")
print_kwargs(name="sakshi",state="telangana")
print_kwargs(name="sakshi",state="telangana",behaviour="monkey")