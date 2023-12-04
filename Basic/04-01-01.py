a=ord('A') #문자를 아스키 코드값으로 변경해주는 함수
mask = 0x0f
print(a)
print("%x" %(a))
print(bin(a))
print("%x" % (a&mask))
print("%x" % (a|mask))#00001111을 통해 지워주고 하는거