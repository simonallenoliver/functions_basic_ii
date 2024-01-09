# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number 
# (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

# def counting_down(num):
#     new_list = []
#     for i in range(num,-1,-1):
#         new_list.append(i)
#     return(new_list)
# print(counting_down(8))

# # Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# # Example: print_and_return([1,2]) should print 1 and return 2

# def print_and_return(my_list=[]):
#     print(my_list[0])
#     return(my_list[1])
# print(print_and_return(my_list=[3,7]))

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

# def first_plus_length(my_list=[]):
#     sum1 = len(my_list) + my_list[0]
#     return(sum1)
# print(first_plus_length(my_list=[5,7,3,4]))

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original 
# list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements,
# have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

# def greater_than_second(my_list=[]):
#     new_list = []
#     sum = 0
#     for i in range(2, len(my_list)):
#         if my_list[i] > my_list[1]:
#             new_list.append(my_list[i])
#             sum += 1
#     if sum == 0:
#         return False
#     else:
#         print(sum)
#         return new_list
# print(greater_than_second(my_list=[2,9,4,4,6,4]))
# print(greater_than_second(my_list=[2,1,4,4,6,4]))

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create
# and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(size,value):
    my_list= []
    for i in range(size):
        my_list.append(value)
    return my_list
print(length_and_value(4,8))
print(length_and_value(5,2))

