def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    dist = 0
    xBits = "{0:b}".format(x)
    yBits = "{0:b}".format(y)
    print(xBits)
    print(yBits)
    max = 0
    if len(xBits) > len(yBits):
        max = len(xBits)
    else:
        max = len(yBits)
    for i in range(max):
        if i >= len(xBits):
            dist += len(yBits) - i
            break
        if i >= len(yBits):
            dist += len(xBits) - i
            break

        if not xBits[i] == yBits[i]:
            dist += 1
    return dist

print("Hamming dist:", hammingDistance(4, 14))