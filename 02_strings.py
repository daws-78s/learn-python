sample_str = "This-is-a-sample-string"
print(sample_str)

# How to access individual characters from a string
print(sample_str[8])

# Slicing
sub_str = sample_str[2:7]
print(sub_str)

sub_str = sample_str[:]
print(sub_str)

sub_str = sample_str[1:]
print(sub_str)

sub_str = sample_str[:5]
print(sub_str)

sub_str = sample_str[::2]
print(sub_str)

# Reverse a string
sub_str = sample_str[::-1]
print("Reversed string:", sub_str)

# Length of a string
len_str = len(sample_str)
print("Length of a string:", len_str)

# Method
sample_str = "hello"
print(sample_str.capitalize()) # "Hello"

# split(), join(), format(), count(), strip(), lstrip(), rstrip()
sample_str = "This is a sample string"
str_split = sample_str.split() # output: list
print(str_split, type(str_split))

join_split_str = " ".join(str_split)
print(join_split_str, type(join_split_str))

count_a = sample_str.count('a')
print(count_a)

sample_str = "    devops is a very good career choice   "
strip_str = sample_str.strip()
print(strip_str)

# Strings are immutable
sample_str = "This is a sample string"
sample_str[-1] = 'G'
print(sample_str)