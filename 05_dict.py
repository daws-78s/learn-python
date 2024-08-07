sample_dict = {1: 1, 2: 4, 3: 9} # dict()
# Keys in dictionary should of immutable datatype
print(sample_dict[3])

sample_dict = {1: 1, 2: 4, 3: 9, 3: 15}
print(sample_dict[3])

sample_dict = {(1, 2, 3, 4): 1, 2: 4, 3: 9}
print(sample_dict[(1, 2, 3, 4)])

sample_dict = {[1, 2, 3, 4]: 1, 2: 4, 3: 9}
print(sample_dict[[1, 2, 3, 4]])