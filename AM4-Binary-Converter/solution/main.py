# Convert to binary, iterative method
def to_binary_iterative(number):
    binary = ""
    while number > 1:
        # The new digit needs to go in front of the existing ones, so we can't use +=
        binary = str(number % 2) + binary
        number //= 2
    binary = str(number) + binary
    return binary


def to_binary_recursive(number):
    if number <= 1:
        return str(number)

    # Integer division preserves all digits, even above floating-point precision.
    return to_binary_recursive(number // 2) + str(number % 2)


if __name__ == "__main__":
    print(to_binary_iterative(6))
    print(to_binary_recursive(6))
