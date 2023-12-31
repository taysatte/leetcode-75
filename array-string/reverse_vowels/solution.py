def reverse_vowels(s: str) -> str:
    """
    Given a string s, reverse only all the vowels in the string and return it.

    :param int s: A given string
    :returns: The given string s with its vowel characters reveresed
    :rtype: String
    """
    vowels_ref = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vowel_stack = []
    out = ""

    # loop over each character in string to find vowels
    for char in s:
        # add char to stack if a vowel
        if char in vowels_ref:
            vowel_stack.append(char)
    # loop over each character again to find non-vowels
    for char in s:
        if char not in vowels_ref:
            out += char
        else:
            out += vowel_stack.pop()
    return out
