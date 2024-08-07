sample_dict = {1: 1, 2: 4, 3: 9} # dict()
# Keys in dictionary should of immutable datatype
print(sample_dict[3])

sample_dict = {1: 1, 2: 4, 3: 9, 3: 15}
print(sample_dict[3])

sample_dict = {(1, 2, 3, 4): 1, 2: 4, 3: 9}
print(sample_dict[(1, 2, 3, 4)])

sample_dict = {"1": 1, 2: 4, 3: 9}
print(sample_dict["1"])

# sample_dict = {[1, 2, 3, 4]: 1, 2: 4, 3: 9}
# print(sample_dict[[1, 2, 3, 4]])

"""
Traceback (most recent call last):
  File "/home/cloudshell-user/python-devops/05_dict.py", line 11, in <module>
    sample_dict = {[1, 2, 3, 4]: 1, 2: 4, 3: 9}
TypeError: unhashable type: 'list'
"""
dict_keys = sample_dict.keys()
dict_values = sample_dict.values()
dict_items = sample_dict.items()
print(dict_keys, dict_values, dict_items)

# What happens if you access a key that is not present inside a dict
sample_dict = {"1": 1, 2: 4, 3: 9}
print(sample_dict.get(1)) # None
# print(sample_dict[1]) # Error

sample_dict = {1: 1, 2: 4, 3: 9}
sample_dict[4] = 16
print(sample_dict)