# How to use break statement
int_list = [1,5,6,4,6,3]

# Find the even value in the given list
for num in int_list:
    print("Current element of the list", num)
    if(num%2==0):
        print("Even number in the list",num)
        break

# How to use continue keyword
# Print the numbers from for loop and start them from value 1
# but print values in terminal if number is greater than 10

for num in range(1,21):  #range(1,21) -> [1,2,3,4,5,6....20]
    if(num<10):
        continue
    print(num)
