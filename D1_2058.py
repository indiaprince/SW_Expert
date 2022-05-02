N = int(input())
total = 0
while(1):
    total+=N%10
    N=N//10
    if(N<1):break
print(total)