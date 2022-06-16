def print_seq(l,n):
    l = ['*',]*(n - len(l)) + list(map(str , l))
    print(' '.join(l))

def haveli_hakini(l):

    n = len(l)
    print("Input : ",end = '')
    print_seq(l , n)
    print()
    flag = 0
    count = 0
    
    while len(l):
        if l == [0]*len(l) :
            break
        l = list(reversed(sorted(l)))
        head = l.pop(0)
        if len(l) == 0:
            break
        print_seq(l,n)
        for i in range(head):

            l[i] -= 1
            if l[i] < 0:
                flag = 1
                break
        if flag == 1:
            break
        else:
            print_seq(l,n)
        count += 1

    if flag == 1:
        print("Graph not possible !")
    else:
        print("Graph is possible !")
l = [8,8,7,6,6,5,5,2,2,2,1,1,1]
haveli_hakini(l)
