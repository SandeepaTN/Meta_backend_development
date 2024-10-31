def count_back(n):
    if n==0:
        return 
    print(n)
    count_back(n-1)
    print(n)

count_back(5)


def count_leaf_items(item_list):
    
    count = 0
    for item in item_list:
        if isinstance(item, list):
            count += count_leaf_items(item)
        else:
            count += 1


    return count


lst=['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
print(count_leaf_items(lst))