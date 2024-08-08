# def sample_func():
#     print("This is a sample function")

# # Call the function
# sample_func()

# def add(num_1, num_2):
#     """
#     This function performs addition of 2 numbers
#     """
#     res = num_1 + num_2
#     return res

# # Call the function
# # res = add(1, 2)
# res = add(num_2=1, num_1=2)
# print(res)

# help(add)

# def add(num_1, num_2, num_3=10):
#     """
#     This function performs addition of 2 numbers
#     """
#     res = num_1 + num_2 + num_3
#     return res

# Call the function
# res = add(1, 2)
# res = add(num_2=1, num_1=2)
# print(res)

# One user enters 10 numbers and another user enters 100 numbers. Define your function to handle this situation
# A: Variable length arguments

# def add(*nums):
#     """
#     This function performs addition of 2 numbers
#     """
#     res = sum(nums)
#     return res

# res = add(1, 2, 4)
# print(res)

# res = add(1, 2, 4, 5, 6)
# print(res)

# def add(num1, num2, *args):
#     """
#     This function performs addition of 2 numbers
#     """
#     res = num1 + num2 + sum(args)
#     return res

# res = add(1, 2, 4, 5)
# print(res)

# res = add(1, 2, 4, 5, 6)
# print(res)

def add(*args, **kwargs):
    """
    This function performs addition of 2 numbers
    """
    print(args, kwargs)

res = add(1, 2, 4)
print(res)

res = add(1, 2, 4, num1=5, num2=6)
print(res)

# map
# filter

# Lambda: inline function

add_numbers = lambda num1, num2: num1 + num2
res = add_numbers(1, 2)
print(res)