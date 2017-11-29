def baseConversion(x, b):
    """
    Converts a base 10 number 'x' to a base 'b' number
    """
    assert(x >= 0)
    assert(1< b < 37)
    r = ''
    import string
    while x > 0:
        r = string.printable[x % b] + r
        x //= b
    return r 


