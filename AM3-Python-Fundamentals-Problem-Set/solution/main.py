"""Fundamentals references with explicit boundaries and quiet imports."""


def _require_integer(N, minimum=0):
    if type(N) is not int or N < minimum:
        raise ValueError("N must be an integer at least " + str(minimum) + ", not bool")


def _require_distinct_nonempty(numbers):
    if not numbers or len(set(numbers)) != len(numbers):
        raise ValueError("a nonempty list of distinct numbers is required")


def double(numbers):
    """Return a new doubled list, preserving input order and duplicates."""
    result = []
    for number in numbers:
        result.append(number * 2)
    return result


def starts_with_a(words):
    """Return words beginning with lowercase a; empty strings do not match."""
    result = []
    for word in words:
        if word and word[0] == "a":
            result.append(word)
    return result


def num_of_evens(numbers):
    """Count even integers, including zero and negative even numbers."""
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


def sum_of_numbers(numbers):
    """Return the numeric sum, or zero for an empty list."""
    total = 0
    for number in numbers:
        total += number
    return total


def index_of_largest_number(numbers):
    """Return the largest-value index in a nonempty distinct-number list."""
    _require_distinct_nonempty(numbers)
    index = 0
    largest_num = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > largest_num:
            index = i
            largest_num = numbers[i]
    return index


def all_squares(N):
    """Print nonnegative perfect squares <= N, one per line; return None."""
    _require_integer(N)
    i = 0
    while i * i <= N:
        print(i * i)
        i += 1


def largest_power_of_two(N):
    """Return the greatest integer x with 2**x <= positive integer N."""
    _require_integer(N, 1)
    i = 0
    power_of_two = 1
    while power_of_two * 2 <= N:
        power_of_two *= 2
        i += 1
    return i


def factorial_sum(N):
    """Return 1! + 2! + ... + N!; zero gives the empty sum."""
    _require_integer(N)
    total = 0
    for i in range(1, N + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        total += factorial
    return total


def largest_divisor(N):
    """Return the largest positive divisor below N, or None at N=1."""
    _require_integer(N, 1)
    for i in range(N - 1, 0, -1):
        if N % i == 0:
            return i
    return None


def largest_product(numbers):
    """Return the maximum product of two distinct positions; require two items."""
    if len(numbers) < 2:
        raise ValueError("largest_product requires at least two integers")
    largest_num = numbers[0] * numbers[1]
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] * numbers[j] > largest_num:
                largest_num = numbers[i] * numbers[j]
    return largest_num


def sums_to_zero(numbers):
    """Return True iff two distinct positions sum to zero; do not reuse an item."""
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == 0:
                return True
    return False


def most_common_numbers(numbers):
    """Return all tied modes in ascending order, or a new empty list."""
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
    return sorted(most_common)


def reverse_string(str):
    """Reverse every character, including whitespace and punctuation."""
    reverse_str = ""
    for i in range(len(str) - 1, -1, -1):
        reverse_str += str[i]
    return reverse_str


def count_vowels(str):
    """Count ASCII a/e/i/o/u in either case; y is not counted."""
    count = 0
    for character in str:
        if character.lower() in ("a", "e", "i", "o", "u"):
            count += 1
    return count


def count_pairs(numbers):
    """Count distinct values whose frequency is exactly two."""
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


def swap_min_max(numbers):
    """Swap extrema in place for a nonempty distinct-number list; return it."""
    _require_distinct_nonempty(numbers)
    min_index = 0
    max_index = 0
    for i in range(len(numbers)):
        if numbers[i] < numbers[min_index]:
            min_index = i
        if numbers[i] > numbers[max_index]:
            max_index = i
    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
    return numbers


if __name__ == "__main__":
    print("double:", double([1, 2, 3]))
    print("starts with a:", starts_with_a(["", "apple", "Apple", "ant"]))
    print("even count:", num_of_evens([-2, 0, 3]))
    print("sum:", sum_of_numbers([-1, 1, 2, 3]))
    print("largest index:", index_of_largest_number([-4, -6, -3]))
    print("squares:")
    all_squares(16)
    print("power:", largest_power_of_two(65))
    print("factorial sum:", factorial_sum(3))
    print("divisor:", largest_divisor(24))
    print("largest product:", largest_product([-3, -8, 10]))
    print("zero pair:", sums_to_zero([-5, 8, 5]))
    print("ordered modes:", most_common_numbers([3, 6, 2, 2, 6]))
    print("reverse:", reverse_string("hello"))
    print("vowels:", count_vowels("Mooncake"))
    print("pairs:", count_pairs([1, 1, 2, 2, 3, 3, 3, 4]))
    print("swapped:", swap_min_max([1, 2, 3, 4]))
