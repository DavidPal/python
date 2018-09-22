import math


def is_prime(x):
    if x <= 1:
        return False

    if x == 2:
        return True

    if x % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(x)) + 1, 2):
        # print("{} {}".format(x, i))
        if x % i == 0:
            return False

    return True


def list_primes():
    for i in range(20):
        print("i = {},  is_prime(i) = {}".format(i, is_prime(i)))


list_primes()
