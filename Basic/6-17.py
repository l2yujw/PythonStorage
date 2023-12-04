import random

rn = random.sample(range(1,10),3)
print(rn)

t_cnt = s_cnt = b_cnt = 0

while(s_cnt < 3) :
    s_cnt = b_cnt = 0
    num = input("중복x 숫자 3자리 입력 ")
    print(num[0], num[1], num[2])
    for i in range(0,3):
        if (num[i] == str(rn[i])) :
            s_cnt+=1
            continue
        elif num[i] in str(rn) :
            b_cnt+=1
            continue
        else :
            continue

    print(s_cnt, "+", b_cnt)
    t_cnt += 1
if(s_cnt == 3):
    print(t_cnt)