#number of elements in the array that are bigger
#then the element b4 them
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range (1,n):
    if a[i]>a[i-1]:
        c+=1
print(c)