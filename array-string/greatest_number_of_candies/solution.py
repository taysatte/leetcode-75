def kids_with_candies(candies: list, extra_candies: int) -> list:
    """
    There are n kids with candies. You are given an integer array candies,
    where each candies[i] represents the number of candies the ith kid has,
    and an integer extraCandies, denoting the number of extra candies that
    you have.

    :param List[int] candies: Integer array where each candies[i] represents
    the number of candies the i^th kid has
    :param int extra_candies: Number of extra candies left over
    :returns: A boolean array result of length n, where result[i] is true if,
    after giving the i^th kid all the extra_candies, they will have the
    greatest number of candies among all the kids, or false otherwise.
    :rtype: List[bool]
    """
    result, is_greatest = [], True

    for kid in range(0, len(candies)):
        val = candies[kid] + extra_candies
        is_greatest = True if val >= max(candies) else False
        result.append(is_greatest)
    return result
