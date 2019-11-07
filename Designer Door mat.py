# Enter your code here. Read input from STDIN. Print output to STDOUT
l = list(map(int,input().split()))
for i in range(1,l[0]+1):
    if i-1 < l[0]//2:
        print('-'*((l[1]-3)//2-3*(i-1))+'.|.'*(2*i-1)+'-'*((l[1]-3)//2-3*(i-1)))
    elif i-1 == l[0]//2:
        print('-'*((l[1]-7)//2)+'WELCOME'+'-'*((l[1]-7)//2))
    else:
        print('-'*((l[1]-3)//2-3*(l[0]-i))+'.|.'*(2*l[0]-(2*i-1))+'-'*((l[1]-3)//2-3*(l[0]-i)))
