sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"]

# for ele in sample_list:
#     print(ele, len(ele))

# Print the element and its corresponding index

# for idx, ele in enumerate(sample_list):
#     print(idx, ele)

# Range based for loop
# 1:10 -> 1,2...,9
sample_range = range(0, len(sample_list))
print(sample_range, type(sample_range))

for idx in sample_range:
    print(idx)