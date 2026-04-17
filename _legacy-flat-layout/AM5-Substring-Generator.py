"""
Write a function that returns a list of all the possible substrings of the input string.
"""


def getSubstrings(string):
	if len(string) == 0:
		return [string]
	substrings = [string]
	
	newSubstrings = substrings
	
	result1 = getSubstrings(string[1:])
	for substr in result1:
		newSubstrings.append(substr)
	
	result2 = getSubstrings(string[:-1])
	for substr in result2:
		newSubstrings.append(substr)
	
	setSubs = set(newSubstrings)  # convert to set to delete duplicates
	substrings = list(setSubs)  # convert back to list
	return substrings


print(getSubstrings("abcde"))
