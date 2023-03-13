n = int(input())
data = list(map(int, input().split()))
data.sort(reverse=True)
print(n)
print(data)

# 입력에 소요되는 시간을 더 줄이기
# sys.stdin.readline() 주의! 입력 후 enter가 줄 바꿈 기호로 입력되므로 rstrip() 메서드 함께 이용

a = 1
b = 2
print(a, b)

# default는 줄바꿈이나 바꿔줄 수 있다.
print(7, end=" ")
print(8, end=" ")
print("sdfsdfs")

# f string
ans = 7
print(f"정답은 {ans}입니다.")