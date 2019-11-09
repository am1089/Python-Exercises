# Create a permutation of a list of elements

def permutations(l):
    stack = []
    if len(l) == 0 or len(l) == 1:
        stack.append(l)
        return stack
    listlen = len(l)
    for i in range(listlen):
        # list(l) makes a copy of the original list
        s = list(l)
        x = s.pop(i)
        n = permutations(s)
        m = [x]
        while len(n) > 0 :
            s = n.pop(0)
            stack.append(m+s)
    return stack

plist = [1,2,3]
lp = permutations(plist)
lperm = len(lp)
for _ in range(lperm):
    x = lp.pop(0)
    print(x)


