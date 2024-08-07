sample_set = {1, 2, 5, 2, 4, 3} # set()
print(sample_set)

# A Set returns unique elements that is stored inside that variable
# Sets don't consider the order of insertion
# Sets don't support indexing

# Add elements to a set
sample_set = {1, 2, 5, 2, 4, 3}
sample_set.add(6)
print(sample_set)
# print(sample_set[2])

""" 
Traceback (most recent call last):
  File "/home/cloudshell-user/python-devops/06_sets.py", line 12, in <module>
    print(sample_set[2])
TypeError: 'set' object is not subscriptable 
"""

# intersection(), union()