# Loop to figure out the largest key beforehand
def countingSort(lst):
    freq = {}
    for num in lst:
        if (num in freq):
            freq[num] += 1
        else:
            freq[num] = 1

    sortMe = list(freq.keys())
    sortedKeys = sorted(sortMe)
    result = []

    for key in sortedKeys:
        result.extend([key] * freq[key])
    return result


# All numbers are strictly less than k
def countingSortLimited(lst, k):
    freq = [0 for _ in range(k)]

    for num in lst:
        freq[num] += 1

    result = []

    for num in range(k):
        result.extend([num] * freq[num])
    return result
