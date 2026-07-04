# Convert to binary, iterative method
def to_binary_iterative(number):
    binary = ""
    while number > 1:
        # The new digit needs to go in front of the existing ones, so we can't use +=
        binary = str(number % 2) + binary
        number = int(number / 2)  # Alternatively, introduce //=
    binary = str(number) + binary
    return binary


print(to_binary_iterative(6))


def to_binary_recursive(number):
    if number <= 1:
        return str(number)

    # Rather than int(number/2), you could alternatively introduce number // 2
    return to_binary_recursive(int(number / 2)) + str(number % 2)


print(to_binary_recursive(6))
