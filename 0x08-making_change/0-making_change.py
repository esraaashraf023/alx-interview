#!/usr/bin/python3
"""Algorithm"""


def makeChange(coins, total):
    """ Given a pile of coins of different values"""
    if total <= 0:
        return 0

    check, steps = 0, 0
    coins.sort(reverse=True)

    for coin in coins:
        while check < total:
            check += coin
            steps += 1

        if check == total:
            return steps

        check -= coin
        steps -= 1

    return -1
