import tabulate

def ext_euc_alg(a,b):
  
    R0 = [1,0]
    R1 = [0,1]
    Q =  [0,a//b]
    D =  [a,b]
    
    table_body = [[D[0] , Q[0] , R0[0] , R1[0]],[D[1] , Q[1] , R0[1] , R1[1]]]
    
    while D[-1]!=0:
        r0 = R0[-2] - Q[-1]*R0[-1]
        r1 = R1[-2] - Q[-1]*R1[-1]
        d = D[-2]%D[-1]
        D.append(d)
        if d == 0:
            break
        q = D[-2]//D[-1]
        R0.append(r0)
        R1.append(r1)
        Q.append(q)
        table_body.append([D[-1] , Q[-1] , R0[-1] , R1[-1]])
    print(tabulate.tabulate(table_body , ["MOD","QUOTIENT" , "R0" , "R1"],tablefmt = "grid"))
    
    
if __name__ == "__main__":
    a,b = list(map(int,input().split()))
    ext_euc_alg(a , b)
