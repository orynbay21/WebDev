import math
v=int(input())
t=int(input())
s=109
put=abs(v)*t
raz=put%s
if(raz==0):
    print(0)
elif(v>0):
    print(raz)
else:
    print(s-raz)
