import random


def decompose(number):
    exponent_of_two = 0

    while number % 2 == 0:
        number /= 2
        exponent_of_two += 1

    return exponent_of_two, number


def is_witness(possible_witness, prime, exponent, remainder):
    possible_witness = pow(possible_witness, int(remainder), prime)

    if possible_witness == 1 or possible_witness == prime - 1:
        return False

    for _ in range(exponent):
        possible_witness = pow(possible_witness, 2, prime)

        if possible_witness == prime - 1:
            return False

    return True


def probably_prime(prime, accuracy=None):
    if accuracy is None:
        accuracy = 100

    if prime == 2 or prime == 3:
        return True

    if prime < 2:
        return False

    exponent, remainder = decompose(prime - 1)

    for _ in range(accuracy):
        possible_witness = random.randint(2, prime - 2)
        if is_witness(possible_witness, prime, exponent, remainder):
            return False

    return True
