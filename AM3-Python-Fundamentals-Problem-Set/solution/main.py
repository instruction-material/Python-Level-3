###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

# (1) Write a function that takes in a list of numbers and returns a list with every number doubled.
def double(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return result


print(double([1, 2, 3]))


# (2) Write a function that takes in a list of words and returns a list of only the words that start with the letter 'a.'
def starts_with_a(words):
    result = []
    for word in words:
        if word[0] == "a":
            result.append(word)
    return result


print(starts_with_a(["apple", "banana", "ant", "orange"]))


# (3) Write a function that takes in a list of numbers and returns the number of even numbers in the list.
def num_of_evens(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


print(num_of_evens([2, 4, 6, 7]))


# (4) Write a function that takes in a list of numbers and returns the sum of the list.
def sum_of_numbers(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


print(sum_of_numbers([-1, 1, 2, 3]))


# (5) Write a function that takes in a list of distinct numbers and returns the index of the largest number in the list.
def index_of_largest_number(numbers):
    index = 0
    largest_num = numbers[0]
    for i in range(0, len(numbers)):
        if numbers[i] > largest_num:
            index = i
            largest_num = numbers[i]
    return index


print(index_of_largest_number([-4, -6, -3]))


# (6) For a given integer N, print all perfect squares less than or equal to N.
def all_squares(N):
    i = 0
    while True:
        perfect_square = i * i
        if perfect_square <= N:
            print(perfect_square)
        else:
            break
        i += 1


all_squares(101)


# (7) Write a function that takes in an integer N and returns the greatest integer x for which 2^x is less than or equal to N.
def largest_power_of_two(N):
    i = 0
    while True:
        power_of_two = 2**i
        if power_of_two > N:
            return i - 1
        i += 1


print(largest_power_of_two(65))


# (8) Write a function that takes in an integer N and returns the sum of 1! + 2! + ... + N!.
def factorial_sum(N):
    sum = 0
    for i in range(1, N + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        sum += factorial
    return sum


print(factorial_sum(3))


# (9) Write a function that takes in a positive integer N and returns its largest divisor less than N.
def largest_divisor(N):
    for i in range(N - 1, 0, -1):
        if N % i == 0:
            return i


print(largest_divisor(24))


# (10) Write a function that takes in a list of integers (positive or negative) and returns the largest product that can be made with any two numbers from the list.
def largest_product(numbers):
    largest_num = numbers[0] * numbers[1]
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if numbers[i] * numbers[j] > largest_num and i != j:
                largest_num = numbers[i] * numbers[j]
    return largest_num


print(largest_product([0, 5, 9]))
print(largest_product([-3, -8, 10]))


# (11) Write a function that takes in a list of integers (positive or negative) and return True if any pair of the numbers in the list sum to 0, Otherwise, return False.
def sums_to_zero(numbers):
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if numbers[i] + numbers[j] == 0 and i != j:
                return True
    return False


print(sums_to_zero([0, -1, 2]))
print(sums_to_zero([-5, 8, 5]))


# (12) Write a function that takes in a list of integers and returns a list of the most commonly occurring integers in the list. For example, if the list is [3, 6, 2, 2, 6], the function should return [2,6].
def most_common_numbers(numbers):
    freq = {}
    for number in numbers:
        if number in freq:
            freq[number] += 1
        else:
            freq[number] = 1
    highest_freq = 0
    most_common = []
    for number in freq:
        if freq[number] > highest_freq:
            most_common = [number]
            highest_freq = freq[number]
        elif freq[number] == highest_freq:
            most_common.append(number)
    return most_common


print(most_common_numbers([6, 3, 2, 2]))
print(most_common_numbers([5, 4, 5, 4, 5, 4]))
print(most_common_numbers([1, 2, 3]))


# (13) Write a function that takes in a string and returns the string in reverse order.
def reverse_string(str):
    reverse_str = ""
    for i in range(len(str) - 1, -1, -1):
        reverse_str += str[i]
    return reverse_str


print(reverse_string("hello"))


# (14) Write a function that takes in a string and returns the number of vowels in the string.
def count_vowels(str):
    count = 0
    for i in str:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            count += 1
    return count


print(count_vowels("mooncake"))


# (15) Write a function that takes in a list of numbers and returns the number of numbers that appear exactly twice in the list.
def count_pairs(numbers):
    freq = {}
    count = 0
    for number in numbers:
        if number in freq:
            freq[number] += 1
        else:
            freq[number] = 1
    for number in freq:
        if freq[number] == 2:
            count += 1
    return count


print(count_pairs([1, 1, 2, 2, 3, 3, 3, 4]))


# (16) Write a function that takes in a list of distinct numbers and return the list with the smallest and largest numbers swapped.
def swap_min_max(numbers):
    min_index = 0
    max_index = 0
    min_num = numbers[0]
    max_num = numbers[0]
    for i in range(0, len(numbers)):
        number = numbers[i]
        if number < min_num:
            min_index = i
            min_num = number
        elif number > max_num:
            max_index = i
            max_num = number
    numbers[min_index] = max_num
    numbers[max_index] = min_num
    return numbers


print(swap_min_max([1, 2, 3, 4]))
