import heapq

li = [4,5,8,9,11,6]

print('Min Heap Operation')
heapq.heapify(li)

print(li)
heapq.heappop(li)
print(li)
heapq.heappop(li)
print(li)
heapq.heappop(li)
print(li)

print('Max Heap Operation')

li = [4,5,8,9,11,6]

li = [i * -1 for i in li]

print(li)
heapq.heapify(li)
print(li)
print(heapq.heappop(li) * -1)
print(li)
print(heapq.heappop(li) * -1)
print(li)
print(heapq.heappop(li) * -1)
print(li)
