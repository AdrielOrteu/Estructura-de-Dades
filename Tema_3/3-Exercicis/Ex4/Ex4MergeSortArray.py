def mergeSortArray(v,indexInici=None,indexFinal=None):
    x = merge_sort(v)
    for i in range(len(v)):
        v[i] = x[i]

def merge_sort(v):
    if len(v) <= 1:
        print("MergeSort-if",v)
        return v
    else:
        x, y = split(v)
        print("MergeSort-else",x,y)
        x = merge_sort(x)
        y = merge_sort(y)
        r = merge(x, y)
        return r

def split(v):
    x=[]
    y=[]
    for i in range(len(v)):
        if i%2==0:
            x.append(v[i])
        else:
            y.append(v[i])
    return x, y

def merge(v, w):
    print("merge-inputs", v, w)
    r = []
    while v and w:
        if v[0] < w[0]:
            r.append(v[0])
            v.pop(0)
        else:
            r.append(w[0])
            w.pop(0)
    r.extend(v)
    r.extend(w)
    print("merge-output", r)
    return r


sorted_list = merge_sort(["c", "a", "b", "d"])
print(sorted_list)