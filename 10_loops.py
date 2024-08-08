sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"]

# for ele in sample_list:
#     print(ele, len(ele))

# Print the element and its corresponding index

# for idx, ele in enumerate(sample_list):
#     print(idx, ele)

# Range based for loop
# 1:10 -> 1,2...,9

# sample_range = range(0, len(sample_list))
# print(sample_range, type(sample_range))

# for idx in range(0, len(sample_list)):
#     print(idx, sample_list[idx])

# for idx in range(0, len(sample_list)):
#     if sample_list[idx] == "Docker":
#         continue
#     print(idx, sample_list[idx])

# for idx in range(0, len(sample_list)):
#     if sample_list[idx] == "Docker":
#         break
#     print(idx, sample_list[idx])

# for idx in range(0, len(sample_list)):
#     if sample_list[idx] == "Docker":
#         pass
#     print(idx, sample_list[idx])

# for idx in range(0, len(sample_list)):
#     if sample_list[idx] == "Docker":
#         exit(1)
#     print(idx, sample_list[idx])

# print(sample_list)

# sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"]

# idx = 0

# while idx < len(sample_list):
#     if sample_list[idx] == "Docker":
#         break
#     print(idx, sample_list[idx])
#     idx += 1

sample_dict = {1: 1, 2: 4, 3: 9}

for k, v in sample_dict.items():
    print(k, v)