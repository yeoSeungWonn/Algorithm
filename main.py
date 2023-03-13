# 전역 변수를 사용할 때는 global

a = 0

def func():
  global a
  a += 1

for _ in range(10):
  func()

print(a)

# 반환 값이 여러 개 

def operator(a, b):
  add = a + b
  sub = a - b
  multiply = a * b
  devide = a / b
  return add, sub, multiply, devide

a, b, c, d = operator(1, 2)
print(a, b, c, d)

# 람다 표현식
print((lambda a, b: a + b) (3, 7))

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

# 1
def my_key(x):
  return x[1]

print(sorted(array, key=my_key))


print(sorted(array, key=lambda x: x[1]))