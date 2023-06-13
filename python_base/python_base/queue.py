# 复杂度是O(n)
# queue = []
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue.pop(0))  # 1
# print(queue.pop(0))  # 2
# print(queue.pop(0))  # 3

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
