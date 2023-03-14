import heapq

pq = [] # 빈 배열을 하나 만든다

heapq.heappush(pq, 456)
heapq.heappush(pq, 123)
heapq.heappush(pq, -1)

# 기본은 최소 힙
while len(pq) > 0:
  print(heapq.heappop(pq))

# 최대힙을 위해서는 부호를 바꿔준다.
heap = []
list = [1, 2, 3, 4, 5]

for i in list:
  heapq.heappush(heap, -i)

for _ in range(len(list)):
  print(-heapq.heappop(heap))