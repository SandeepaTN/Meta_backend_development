def add_to_list(lst,itm):
    n_lst=lst.copy()
    n_lst.append(itm)
    return n_lst

l=[1,6,5,4]
nl=add_to_list(l,7)
print(l)
print(nl)

s='samdy'
print(s[::-1])