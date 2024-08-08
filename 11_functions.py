# def sample_func():
#     print("This is a sample function")

# # Call the function
# sample_func()

def add(num_1, num_2):
    """
    This function performs addition of 2 numbers
    """
    res = num_1 + num_2
    return res

# Call the function
# res = add(1, 2)
res = add(num_2=1, num_1=2)
print(res)

help(add)