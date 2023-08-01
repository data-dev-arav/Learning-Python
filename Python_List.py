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

# How to check if list are equal to each other
list1 = [1,"Arvind",20,"Hi"]
list2 = [1,"Arvind",20,"Hi"]
print("List are equal or not ?",list1==list2)

list1 = [1,"Arvind",20,"Hi"]
list2 = [1,"Arivnd","Hi",20]
print("List are equal or not ?", list1==list2)


# List concat
list4 = [1,2,3,4,5]
list5 = [100,200,300,400,500]
result = list4 + list5
print(result)

# How to update the value of list index item?

list7 = [1,"Arvind", 1000]

# Difference between append() and extend()

list8 = [1,2,3,'Arvind', [6,6,6], "Rahul"]
print(len(list8))

list9 = [20,30,40]
list10 = ['Hi','Hello','Bye']
result1=list9.append(list10)
print("Output of append",list9)

list11 = [20,30,40]
list12 = ['Hi','Hello','Bye']
result2=list11.extend(list12)
print("Output of extend",list11)


# List slicing
list13 = [20,30,40,50,60,70,80]

print(list13[0:])
print(list13[3:])

print(list13[:])
# End index is always exclusive
print(list13[0:3])

print(list13[2:6])

print(list13[0::2]) # 3rd value is for step

# How to print the last value of the index
print(list13[-1]) 

# Print list in revers direction
print(list13[-1 : : -1])
