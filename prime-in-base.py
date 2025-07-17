def basify(num, base):
    powers = [1]
    while powers[-1] <= num:
        powers.append(powers[-1] * base)
    out = ""
    while len(powers) > 0:
        out += str(int(num / powers[-1]))
        num -= powers[-1] * int(num / powers[-1])
        powers = powers[:-1]
    return int(out[1:])

import math

def is_prime(num):
    check = 2
    while check <= math.sqrt(num):
        if num % check == 0:
            return False
        else:
            check += 1
    return True

def is_prime_in_base(num, base):
    return is_prime(basify(num, base))
