###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

# Create a list of the numbers 1 through 20 (without hard-coding the list)
nums = []
for i in range(20):
    nums.append(i + 1)
print(nums)

# Create a list of the first 10 even numbers (without hard-coding the list)
evens = []
for i in range(1, 21):
    if i % 2 == 0:
        evens.append(i)
print(evens)

# Create a list of the first 10 perfect squares (without hard-coding the list)
squares = []
for i in range(1, 11):
    squares.append(i * i)
print(squares)


# Write a function that takes in two lists and returns the sum of both lists
def sum_lists(l1, l2):
    answer = 0
    for num in l1:
        answer += num
    for num in l2:
        answer += num
    return answer


a = [3, 5, 3, 2, -4, 1]
b = [4, 8, 9, -3, -5]
print(sum_lists(a, b))


# Write a function that takes in a list and returns the minimum value in that list
def minimum(l):
    min_num = l[0]
    for num in l:
        if num < min_num:
            min_num = num
    return min_num


print(minimum(a))


# Write a function that takes in a list and returns the maximum value in that list
def maximum(l):
    max_num = l[0]
    for num in l:
        if num > max_num:
            max_num = num
    return max_num


print(maximum(a))


# Write a function that takes in a list of lists, and returns the sum of all those lists
def sum_list_of_lists(l):
    answer = 0
    for element in l:
        for num in element:
            answer += num
    return answer


l = [[1, 2, 3], [4, 5, 6], [], [7, 8, 9]]
print(sum_list_of_lists(l))


# Write a function that takes in a list of lists, and returns a new list made from “flattening” the lists (putting every element from each list into a single list)
def flatten_list(l):
    new_list = []
    for element in l:
        for num in element:
            new_list.append(num)
    return new_list


print(flatten_list(l))


# Write a function that takes in a list of lists that returns a new list of all the individual maxes from each list. Can you find a way to use the function that you already made that returns the maximum of a list?
def max_list(l):
    m_list = []
    for i in range(len(l)):
        if len(l[i]) > 0:
            m_list.append(maximum(l[i]))
    return m_list


print(max_list(l))
