import random
import time

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]
print
while True:
    print(lunch)
    item = input("음식을 추가 해주세요 (없으면 q를 눌러주세요)  : ")
    if(item == "q"):
        break
    else:
        lunch.append(item)
print(lunch)

set_lunch = set(lunch)     # 집합으로 변환 (삭제할 음식은 집합-집합으로 해보기 위해서)


while True:
    print(set_lunch)
    item = input("음식을 삭제해주세요 (없으면 q를 눌러주세요) : ")
    if(item == "q"):
        break
    else:
        set_lunch = set_lunch - set([item])

print(set_lunch, "중에서 선택합니다.")

for i in range(5,0,-1):
    print(i)
    time.sleep(1)
    
print(random.choice(list(set_lunch)))