def gcd_of_strings(str1: str, str2: str) -> str:
    """
    Given two strings str1 and str2, returns the largest string x such that
    x divides both str1 and str2.

    :param str str1: String 1
    :param str str2: String 2
    :returns: Largest string x that divides both str1 and str2
    :rtype: String
    """
    from math import gcd

    if (str1 + str2) != (str2 + str1):
        return ""
    return str1[:gcd(len(str1), len(str2))]
