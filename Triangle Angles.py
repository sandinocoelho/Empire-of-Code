import math

def cosss(a, b, c):
        return math.degrees(math.acos((c**2-b**2-a**2)/(-2.0 * a * b)))

def angles(a, b, c):
    if a == b and  a == c and b == c:
        return [60, 60, 60]
    else:
        angA = round(cosss(a, b, c))
        angB = round(cosss(b, c, a))
        angC = round(cosss(c, a, b))
        list = [angA,angB,angC]
        list.sort()
        return list



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert angles(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert angles(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert angles(2, 2, 5) == [0, 0, 0], "It can not be a triangle"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
