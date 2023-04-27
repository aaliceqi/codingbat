def diff21(n):
    """
    
    Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
    """

    import math
    if n > 21:
        return abs(n-21)**2
    else:
        return abs(n-21)

print(diff21(19) )
print(diff21(10) )
print(diff21(21))