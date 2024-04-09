def remove_dups(l1,l2):
    for e in l1:
        if e in l2:
            l1.remove(e)

l1 = [1,2,3,4,5]
l2 = [2,3]
remove_dups(l1,l2)
print(l1)

def remove_dups_c(l1,l2):
    l1_copy = l1[:]
    for e in l1_copy:
        if e in l2:
            l1.remove(e)

l1_c = [1,2,3,4,5]
l2_c = [2,3]
remove_dups_c(l1_c,l2_c)
print(l1_c)