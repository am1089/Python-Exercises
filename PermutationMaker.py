# Create a permutation of a list of elements

def permutations(l):
    if len(l) == 0 or len(l) == 1:
        yield l
        return
    listlen = len(l)
    for i in range(listlen):
        # list(l) makes a copy of the original list
        s = list(l)
        x = s.pop(i)
        n = permutations(s)
        m = [x]
        for s in n:
            yield m+s
    return

plist = [1,2,3]
for x in permutations(plist):
    print(x)
