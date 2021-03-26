# all unique.py
#  check if list has duplicates

def all_unique(list):
    # use set() to remove them and compare list length
    # return false if not equal length
    return len(list) == len(set(list))

x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
print(all_unique(x))
