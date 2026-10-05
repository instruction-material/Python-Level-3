"""Advanced-sort/file review reference. Traces and explanations are in README.md."""


def bubbleSort(lst):
    for i in range(0, len(lst)):
        for j in range(0, len(lst) - 1):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
    return lst



def bubble_sort(lst):
    """Stable ascending in-place sort with an actual no-swap early cutoff."""
    for end in range(len(lst) - 1, 0, -1):
        swapped = False
        for j in range(end):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst


def merge(listA, listB):
    """Stable, indexed linear merge; already sorted inputs are unchanged."""
    result = []
    left = right = 0
    while left < len(listA) and right < len(listB):
        if listA[left] <= listB[right]:
            result.append(listA[left])
            left += 1
        else:
            result.append(listB[right])
            right += 1
    result.extend(listA[left:])
    result.extend(listB[right:])
    return result


def partition(lst, pivot):
    less, eq, great = [], [], []
    for value in lst:
        if value < pivot:
            less.append(value)
        elif value == pivot:
            eq.append(value)
        else:
            great.append(value)
    return less, eq, great


def write_letters(word, path="file.txt"):
    """Validate the word before opening an output file."""
    if not isinstance(word, str) or "\n" in word or "\r" in word:
        raise ValueError("word must be a string without CR/LF")
    with open(path, "w", encoding="utf-8", newline="\n") as output:
        for letter in word:
            output.write(letter + "\n")


def read_letter_counts(path="file.txt"):
    """Count exact characters without stripping meaningful spaces."""
    counts = {}
    with open(path, encoding="utf-8") as source:
        for number, line in enumerate(source, 1):
            letter = line.removesuffix("\n")
            if len(letter) != 1:
                raise ValueError("line " + str(number) + " must contain one character")
            counts[letter] = counts.get(letter, 0) + 1
    return counts


def main():
    word = input("Please enter a word: ")
    write_letters(word)
    print(read_letter_counts())


if __name__ == "__main__":
    main()
