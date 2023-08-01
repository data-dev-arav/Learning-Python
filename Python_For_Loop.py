# write a code to print numbers from 1 to 10.

for num in range(1,10):
    print(num)

# Write a code to print numbers from 1 to 10 using 2 steps
# Example to print odd numbers starting from value 1
for num in range(1,11,2):
    print(num)

# Write a program to print numbers from 10 to 1
for num in range(10,0,-1):
    print(num)


# Write a program to calculate the sum of given list elements using for loop
int_list = [4,8,-2,10,5]
list_sum=0
for num in int_list:
    list_sum+=num
print("Total sum of elements =",list_sum)
