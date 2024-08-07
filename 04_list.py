# Create a list

sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"] # list()

# Indexing, slicing
sample_ele = sample_list[1]
print(sample_ele)

sample_ele = sample_list[5]
print(sample_ele)

sample_ele = sample_list[len(sample_list) - 1] # sample_list[-1]
print(sample_ele)

# Slicing
sliced_list = sample_list[1:3] # ("Terraform", "Jenkins")
print(sliced_list)

sliced_list_len = len(sliced_list)
print(sliced_list_len)

sample_list[1] = "Shell"
print(sample_list)