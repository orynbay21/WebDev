n=int(input())
a=list(map(int,input().split()))
for i in range(1,len(a)):
    if (a[i] >0 and a[i-1]>0) or (a[i]<0 and a[i-1]<0):
        print("YES")
        exit()
print("NO")
"""
Необходимо вывести слово YES, 
если существует пара соседних 
элементов с одинаковыми знаками

"""
