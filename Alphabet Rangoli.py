def print_rangoli(size):
    # your code goes here
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    l = ((size-1)*4+1)      #length of the array
    h = 2*size-1              #height of the array
    for i in range(1,h+1):
        if i <= (h-1)//2+1:
            print('-'*((l-1-4*(i-1))//2),end = '')
            for j in range(1,2*i):
                if j < 2*i//2:
                    print(alpha[size-j]+'-',end = '')
                elif j == 2*i//2:
                    print(alpha[size-j],end = '')
                else:
                    print('-'+alpha[size-2*i//2+(j-2*i//2)],end = '')
            print('-'*((l-1-4*(i-1))//2))
            fina = i
        else:
            print('-'*2*(i-fina),end = '')
            new_for_range = (l-4*(i-fina)+1)//2+1
            for j in range(1,new_for_range):
                if j < new_for_range//2:
                    print(alpha[size-j]+'-',end = '')
                elif j == new_for_range//2:
                    print(alpha[size-j],end = '')
                    fina2 = j
                else:
                    print('-'+alpha[size-fina2+(j-fina2)],end = '')
            print('-'*2*(i-((h-1)//2+1)))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
