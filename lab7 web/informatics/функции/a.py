def min(a,b,c,d):
    min = a
    if min>b:
        min=b
    if min>c:
        min = c
    if min>d:
        min = d
    print(min)
a, b, c, d = map(int,input().split())
min(a,b,c,d)
#Необходимо вывести  наименьшее из 4-х данных чисел.