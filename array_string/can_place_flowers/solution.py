def can_place_flowers(flowerbed: list, n: int) -> bool:
    """
    Given an integer array flowerbed containing 0's and 1's, where 0 means
    empty and 1 means not empty, and an integer n, return true if n new flowers
    can be planted in the flowerbed without violating the no-adjacent-flowers
    rule and false otherwise.

    :param List[int] flowerbed: Integer array containing only 0's and 1's.
    :param int n: Number of new flowers to be planted.
    """
    for i in range(len(flowerbed)):
        # if current spot has no flower planted and the number of flowers to
        # be planted is greater than 0, plant a flower
        if flowerbed[i] == 0 and n > 0:
            flowerbed[i] = 1
            n -= 1
            # check first element
            if i > 0 and flowerbed[i - 1] != 0:
                flowerbed[i] = 0
                n += 1
            # check last element
            elif i < len(flowerbed) - 1 and flowerbed[i + 1] != 0:
                flowerbed[i] = 0
                n += 1
    # if number of flowers to be planted == 0 return true
    # otherwise false
    return n == 0
