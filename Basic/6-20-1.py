import random

print("주택복권생성기")
print("게임수를입력하세요")

num = int(input("게임수 : "))

for i in range(1, num+1) :
    lotto = random.sample(range(0, 10), 6)
    lotto.sort()
    print(lotto)