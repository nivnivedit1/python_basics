# Generator function with yield
#Problem:write a generator function that yields even numbers upto a specified limit.
#####################ABOUT YIELD keyword##################
#The `yield` keyword in Python is like a return, but it pauses the function instead of stopping it completely. 
#It’s used to create generators, which produce one item at a time, saving memory.
#The yield keyword in Python is used to create generators, 
#which are helpful in scenarios like reading large files line by line without loading the entire file into memory.
# def read_large_file(file_path):
#     with open(file_path, 'r') as file:
#         for line in file:
#             yield line.strip()  # Yields one line at a time

# # Using the generator
# for line in read_large_file('large_file.txt'):
#     print(line)  # Processes each line without loading the whole file
def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i
for num in even_generator(10):
    print(num)
