data = dict()
data["사과"] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if "사과" in data:
  print("apple")

key_list = data.keys()

value_list = data.values()

print(key_list)
print(value_list)

for key in key_list:
  print(data[key])


# 집합 자료형 - 중복 X
data = set([1, 2, 3])
data.update([2, 3, 4])

print(data)
