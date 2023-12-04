a=100
result=0
i=0

for i in range(1,5) :
    result = a << i
    print("%d << %d = %d" % (a, i , result))

for i in range(1,5) :
    result = a >> i
    print("%d >> %d = %d" % (a, i , result))

a=b=c=d=20
print(a,b,c,d)

print(int('0011',2))