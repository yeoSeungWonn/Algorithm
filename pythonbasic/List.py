a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

print(a[3])

# 크기가 n이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

# 0부터 9까지의 수를 포함하는 리스트
array = [i for i in range(10)]
print(array)

# N * M 크기의 2차원 리스트 초기화 (잘못된 방법)
n = 4
m = 3
array = [[0] * m] * n
print(array)

array[1][1] = 5
print(array)

# N * M 크기의 2차원 리스트 초기화
n = 4
m = 3
array = [[0] * m  for _ in range(n)]
print(array)

# 반복해서 더하기
sum = 0
for i in range(1, 10):
  sum += i
print(sum)

# 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_) 사용
for _ in range(5):
  print("Hello World")

# 리스트에서 특정 값을 가지는 원소를 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)