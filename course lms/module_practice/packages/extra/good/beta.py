"""beta's"""


def this_beta(i):
    if i <= 1:
        return 1
    return i + this_beta(i-1)

