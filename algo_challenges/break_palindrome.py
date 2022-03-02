"""
In this challenge you will be given a palindrome that you must modify if possible. Chance exactly one character of the string to another character in the range asci[a-z] so that the strring meets the following two conditions
    1. the new string is not a palindrome
    2. the new string is lower lexicographically (alphabetically) than the initial string
    3. The new string is the lowest value string lexicographically that can be created from the original palindrome after making only one change

a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
"""

def break_palindrome(palindrome: str = ''):
    for i in range(len(palindrome) // 2): # quotient without remainder
        if palindrome[i] != 'a':
            return palindrome[:i] + 'a' + palindrome[i+1:]
            """
            all elements before current iteration index + 'a' + the rest of the elements
            """
    return palindrome[:-1] + 'b' if palindrome[:-1] + 'b' < palindrome else "IMPOSSIBLE"
    """
    replace last element with 'b' if result is lower lexicographically than OG string
    """


print(break_palindrome('bab'))
print(break_palindrome('aababaa'))
print(break_palindrome('acca'))
print(break_palindrome('aacaa'))
print(break_palindrome('aaabaaa'))
print(break_palindrome('baaab'))
print(break_palindrome('aaa'))