#n- number of elements in the array<=100
#через пробел записаны Н чисел элементы массива
#all array elements with even indeces including 0
n=int(input())
a=list(map(int,input().split()))
print(*a[::2]) # выводит индексы делящиеся без остатка на 2
