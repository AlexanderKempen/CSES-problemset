def weirdalgorithm(x:int) -> int:
    output = []
    while x != 1:
        if x % 2 == 0:
            x = x/2
            output.append(x)
        else:
            x = (x*3)+1
            output.append(x)

    return output



