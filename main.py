# Python program to swap two variables

x = 5
y = 10

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')
#We will use f' string to test merging on two branches

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print(f'The value of x after swapping is {x}') 
print(f"The value of y after swapping is {y}")
