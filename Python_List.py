# Lists in Python
# It stores heterogenous kind of data
# Sequential data
# Stored in contigous memory location

# Declare empty list
L1 = []
print(type(L1))

# Insert value in list
L1.append(2)
L1.append(3)
L1.append(5)
print(L1)

# Create a list of 1000 numbers start from 1 to 1000
int_list = []
for num in range(1, 1001):
    int_list.append(num)


# How to calculate length of a list ?
len_of_list = len(L1)
print(len_of_list)
