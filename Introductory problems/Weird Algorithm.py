def weirdalgorithm(x:int) -> int:
    if x == 1:
        return x
    else:
        if x % 2 == 0:
            x = x/2
            weirdalgorithm(x)

        else:
            x = (x*3)+1
            weirdalgorithm(x)
