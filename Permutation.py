# Inspired by a C++ variant of permutations

def permutations(str, prefix):
    lenstr = len(str)
    if lenstr == 1:
        print(prefix + str)
    else:
        for i in range(1,lenstr+1):
            rem = str[0:i-1] + str[i:]
            m = str[i-1]
            permutations(rem, prefix + [m])

    return

plist=[1,2,3]
permutations(plist, [])
