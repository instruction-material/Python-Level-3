"""List practice references; loops generate values and imports do not print."""


def make_numbers():
    """Return a fresh list of integers 1 through 20."""
    nums = []
    for i in range(20):
        nums.append(i + 1)
    return nums


def make_evens():
    """Return a fresh list of twenty positive even numbers, 2 through 40."""
    evens = []
    for i in range(1, 21):
        evens.append(2 * i)
    return evens


def make_squares():
    """Return a fresh list of ten positive perfect squares, 1 through 100."""
    squares = []
    for i in range(1, 11):
        squares.append(i * i)
    return squares


def sum_lists(l1, l2):
    """Return the sum of both lists, preserving inputs; empty sums are zero."""
    answer = 0
    for num in l1:
        answer += num
    for num in l2:
        answer += num
    return answer


def minimum(l):
    """Return the minimum of a nonempty numeric list, without mutation."""
    if not l:
        raise ValueError("minimum requires a nonempty list")
    min_num = l[0]
    for num in l:
        if num < min_num:
            min_num = num
    return min_num


def maximum(l):
    """Return the maximum of a nonempty numeric list, without mutation."""
    if not l:
        raise ValueError("maximum requires a nonempty list")
    max_num = l[0]
    for num in l:
        if num > max_num:
            max_num = num
    return max_num


def sum_list_of_lists(l):
    """Return the sum of all inner lists; empty outer/inner lists add zero."""
    answer = 0
    for element in l:
        for num in element:
            answer += num
    return answer


def flatten_list(l):
    """Return a new one-level ordered flattening; preserve all input lists."""
    new_list = []
    for element in l:
        for num in element:
            new_list.append(num)
    return new_list


def max_list(l):
    """Return maxima of nonempty inner lists in order, skipping empty ones."""
    m_list = []
    for inner in l:
        if inner:
            m_list.append(maximum(inner))
    return m_list


if __name__ == "__main__":
    print("numbers:", make_numbers())
    print("twenty positive evens:", make_evens())
    print("ten positive squares:", make_squares())
    a = [3, 5, 3, 2, -4, 1]
    b = [4, 8, 9, -3, -5]
    nested = [[1, 2, 3], [4, 5, 6], [], [7, 8, 9]]
    print("two-list sum:", sum_lists(a, b))
    print("minimum/maximum:", minimum(a), maximum(a))
    print("nested sum:", sum_list_of_lists(nested))
    print("flattened:", flatten_list(nested))
    print("nonempty inner maxima:", max_list(nested))
