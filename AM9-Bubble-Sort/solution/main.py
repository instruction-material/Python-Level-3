def bubble_sort_in_place(values):
    """Sort values in place using the basic bubble sort algorithm."""
    for pass_index in range(len(values)):
        for index in range(0, len(values) - 1 - pass_index):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = (
                    values[index + 1],
                    values[index],
                )

    return values


def bubble_sort_improved(values):
    """Sort values in place and stop early when a pass makes no swaps."""
    for pass_index in range(len(values)):
        swapped = False

        for index in range(0, len(values) - 1 - pass_index):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = (
                    values[index + 1],
                    values[index],
                )
                swapped = True

        if not swapped:
            break

    return values


def bubble_sort_copy(values):
    """Return a sorted copy so the original list remains unchanged."""
    result = values.copy()
    bubble_sort_improved(result)
    return result


sample_values = [42, 17, 17, 99, 8, 63, 21, 5]
copy_sorted = bubble_sort_copy(sample_values)
in_place_values = sample_values.copy()

print("original:", sample_values)
print("sorted copy:", copy_sorted)
print("original after copy sort:", sample_values)
print("in-place sorted:", bubble_sort_improved(in_place_values))

"""
Python can swap two list elements in one statement:

values[index], values[index + 1] = values[index + 1], values[index]

The two right-side values are read before either left-side assignment is stored,
so no temporary variable is needed. This is equivalent to the longer three-step
swap, but it is shorter and avoids naming an extra variable.
"""
