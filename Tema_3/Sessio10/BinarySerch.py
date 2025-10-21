def binarySerchRec(l, val):
    if len(l) == 0:
        return False
    elif list[len(l)//2] > val:
        return binarySerchRec(l[:len(l)//2], val)
    elif list[len(l)//2] < val:
        return binarySerchRec(l[len(l)//2:], val)
    else:
        return l

def binarySerchIter(l, val):
    p1 = 0
    p2 = len(l)-1
    i = len(l)//2
    while l[i] != val:
    