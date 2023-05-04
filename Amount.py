# Name: Joshua Jansen
# OSU Email: Jansejos@oregonstate.edu
# Course: CS325
# Assignment: 5

def amount(A, S):
    """
    Finds the combination of numbers in an array that equals the given target value.
    :param A: Array of integers to be summed together.
    :param S: Target integer.
    :return: An array of nested arrays with the nested array integer values equalling the :param S: integer.
    Nested arrays with the same number combination are removed. If no combination is possible an empty array
    is returned.
    """
    A.sort()
    result = amount_helper(A, S, 0, [], [])
    res = []
    for i in result:
        if i not in res:
            res.append(i)
    return res[::-1]


def amount_helper(array, remainder, start, combination, result):
    """
    Helper function for amount(), uses recursion to find the correct combinations that equal the target value.
    :param array: Array of integers to be summed together.
    :param remainder: The remainder of the target number after subtracting the current value being considered, starts
    at the value of the target number.
    :param start: Starting integer value for the for loop.
    :param combination: Current combination of integers from :param array: that are being considered.
    :param result: The combination of integers that leave :param reminder: at 0.
    :return: An array of nested arrays with the nested array integer values resulting in the :param remainder:
    being equal to 0. If no combination is possible an empty array is returned.
    """
    if remainder == 0:
        return result.append(combination[:])

    if remainder < 0:
        return

    for i in range(start, len(array)):
        combination.append(array[i])
        amount_helper(array, remainder - array[i], i + 1, combination, result)
        combination.pop()

    return result

