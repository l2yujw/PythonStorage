import random

print("주택복권생성기")
print("게임수를입력하세요")

num = int(input("게임수 : "))

for i in range(1, num+1) :
    lotto = [0, 0, 0, 0, 0, 0]

    lottolotto = []
    count = 0
    while count<6 :
        lotto[count] = random.randrange(0, 10, 1)
        if(lotto[count] in lottolotto) :
            continue
        else :
            lottolotto.append(lotto[count])
            count+=1

    lotto.sort()
    print(lotto)