# There are 2 methods to create a tuple
# 1. ()
# 2. tuple()
# Behavior: They're immutable
sample_tuple = ("Ansible", "Terraform", "Jenkins", "Docker", "K8s") # Tool set

sample_ele = sample_tuple[1]
print(sample_ele)

sample_ele = sample_tuple[-1]
print(sample_ele)

# Slicing
sliced_tuple = sample_tuple[1:3] # ("Terraform", "Jenkins")
print(sliced_tuple)