# elements with even indeces excluding 0
n=int(input())
a=list(map(int,input().split()))
print(*[i for i in a if i%2==0])