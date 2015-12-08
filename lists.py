# list methods

my_list1 = ['one', 'two', 'three', 'four']  # list of strings
my_list2 = [1, 2, 3, 4]  # list of ints

my_list1.append('five')
# append adds something to the end of a list
# equivalent to list[len(list):] = [x]

my_list1.extend(['six', 'seven'])
# appends multiple items to a list
# equivalent to list[len(list):] = L

my_list1.insert(0, 'zero')
# inserts an element into a list using arguments (index, element)
# insert(0, x) inserts at the beginning of a list
# insert(len(list), x) is equivalent to append(x)

my_list1.remove('seven')
# remove the first matching item from a list
# if no such item exists, it is an error

my_list1.pop()
# removes and returns the popped item
# defaults to the last item on the list if no index specified
# can specify an index using list.pop([i])
# the [] around i denote that this parameter is optional
# so you would just type list.pop(0) instead of ([0])

my_list1.clear()
# removes all items from the list
# equivalent to del list[:]

my_list2.index(4)
# returns the index of the first item with a value matching the argument
# if no such item exists, it is an error

my_list2.count(1)
# returns the number of times the argument appears in the list

my_list2.sort()
# sorts the items of a list in place

my_list2.reverse()
# reverse the elements in the list in place

my_list2.copy()
# returns a shallow copy of a list
# equivalent to list[:]