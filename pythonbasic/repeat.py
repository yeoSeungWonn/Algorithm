i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
  result += i
  i += 1

print(result)

 # 특정 번호의 학생은 제외한다
score = [90, 85, 77, 65, 97]
cheating_student_list = (2, 4)

for i in range(5):
  if i in cheating_student_list:
    print(score[i])