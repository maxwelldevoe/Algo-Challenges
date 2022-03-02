"""
generate all permutations of an array
"""

#------------------
# Recursive
#------------------

def all_perms(list):
    if len(list) <=1:
        yield list
    else: # wrap this in a conditional to avoid a max recursion depth error
        for perm in all_perms(list[1:]):
            for i in range(len(list)):
                yield perm[:i] + list[0:1] + perm[i:]

result = all_perms([1])
for i in sorted(result):
    print(i)



#------------------
# Iterative
#------------------

def swap(elements, i, j):
    elements[i], elements[j] = elements[j], elements[i]

def generate_permutations(elements, n):
    c = [0] * n
    yield elements
    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                swap(elements, 0, i)
            else:
                swap(elements, c[i], i)
            yield elements
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    

def permutations(elements):
    return generate_permutations(elements, len(elements))

res = permutations([1,2,3])
for r in res:
    print(r)