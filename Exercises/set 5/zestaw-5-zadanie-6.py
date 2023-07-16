import math


def add(z1, z2):
    return (z1[0] + z2[0], z1[1] + z2[1])


def sub(z1, z2):
    return (z1[0] - z2[0], z1[1] - z2[1])


def mul(z1, z2):
    return (z1[0] * z2[0] - z1[1] * z2[1], z1[0] * z2[1] + z1[1] * z2[0])


def div(z1, z2):
    return ((z1[0] * z2[0] + z1[1] * z2[1]) / (z2[0] ** 2 + z2[1] ** 2),
            (z1[1] * z2[0] - z1[0] * z2[1]) / (z2[0] ** 2 + z2[1] ** 2))


def exp(z1, p):
    return ((z1[0] ** 2 + z1[1] ** 2) ** (p / 2) * math.cos(math.acos(z1[0] / (z1[0] ** 2 + z1[1] ** 2) ** 0.5 * p))), (
                z1[0] ** 2 + z1[1] ** 2) ** (p / 2) * math.sin(math.asin(z1[0] / (z1[0] ** 2 + z1[1] ** 2) ** 0.5 * p))

print(add((4, 0), (2, 0)))
print(sub((4, 0), (2, 0)))
print(mul((4, 0), (2, 0)))
print(div((4, 0), (2, 0)))