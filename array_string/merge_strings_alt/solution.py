def merge_strings_alt(word1: str, word2: str) -> str:
    """
    Merges two strings (word1 & word2) by adding letters in alternating order,
    starting with word1. If a string is longer than the other, append the
    additional letters onto the end of the merged string.

    :param str word1: Input string 1
    :param str word2: Input string 2
    :returns: Merged string result of word1 & word2
    :rtype: String
    """

    stck1, stck2 = [], []

    for i in range(0, len(word1)):
        stck1.append(word1[i])
    for j in range(0, len(word2)):
        stck2.append(word2[j])

    merged = ""
    while stck1 and stck2:
        pop_vals = stck1.pop(0) + stck2.pop(0)
        merged += pop_vals

    while stck1:
        merged += stck1.pop(0)

    while stck2:
        merged += stck2.pop(0)

    return merged
