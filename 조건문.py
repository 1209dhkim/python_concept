'''
# 성적 관리 프로그램
# A : 100~91
# B : 90~81
# C : 80~71
# D : 70~61
# F : 60~
# 입력 : 점수, 출력 : 등급
score=int(input("점수를 입력하세요: "))
if 100>=score and 91<=score:
    grade="A"
elif 90>=score and 81<=score:
    grade="B"
elif 80>=score and 71<=score:
    grade="c"
elif 70>=score and 61<=score:
    grade="D"
else:
    grade="F"
print(f'점수 = {score}, 등급={grade}')

if grade=="F":
   print("재수강 하세요")
else :
    print("잘했어요")

'''
import random # random 패키지 사용
num=int(input("숫자를 입력하세요:"))
f=random.randrange(1,110) # 1이상 10미만의 숫자를 랜텀 생성
if f==num:
   print("정답")
else:
    print("오답")
print(f"정답 {f}입니다")
