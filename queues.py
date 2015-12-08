# queues can be made with lists, but it is not efficient
# appends and pops from the end of a list are fast, no shifting required
# appends and pops from the beginning of the list require shifting the list
# collections.deque is a more efficient option for queues

from collections import deque

my_queue = deque([1, 2, 3, 4, 5])
# initial queue

my_queue.append(6)
my_queue.append(7)
# add 6 then 7 to the end of the queue

my_queue.popleft()
my_queue.popleft()
# returns the next item in the queue, ie the first item in the list