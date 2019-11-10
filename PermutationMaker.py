# Create a permutation of a list of elements

def permutations(l):
    if len(l) == 0 or len(l) == 1:
        yield l
        return
    listlen = len(l)
    # Create a sublist by popping one element at a time
    for i in range(listlen):
        # list(l) makes a copy of the original list
        sublist = list(l)
        x = sublist.pop(i)
        m = [x]
        for s in permutations(sublist):
            yield m+s
    return

plist = [1,2,3]
for x in permutations(plist):
    print(x)
