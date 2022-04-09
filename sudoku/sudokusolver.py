import time

size = 9
sz = int(size**0.5)
count = 0

def calc(inp,i,j):
    possible = [i for i in range(1,size+1)]
    # check row
    for x in range(size):
        if inp[x][j]!=0 and x!=i and inp[x][j] in possible:
            possible.remove(inp[x][j])
    # check column
    for x in range(size):
        if inp[i][x]!=0 and x!=j and inp[i][x] in possible:
            possible.remove(inp[i][x])
    # check grid
    for x in range((i//sz)*sz,((i//sz)*sz)+sz):
        for y in range((j//sz)*sz,(j//sz)*sz+sz):
            if inp[x][y]!=0 and x!=i and y!=j and inp[x][y] in possible:
                possible.remove(inp[x][y])
    return possible

def no_filled(inp):
    count1 = 0
    for i in inp:
        for j in i:
            if j!=0:
                count1+=1
    return count1

def valid(inp):
    
    for i in range(size):
        for j in range(size):
            if inp[i][j] ==0 or inp[i][j] in calc(inp,i,j):
                
                continue
            else:
                
                return False
    return True
            
def solve(inp,start,delay_time = 10):
    if time.time()>start + delay_time:
        return
    # all number position right
    if no_filled(inp) == size*size:
        return inp
    found = 0
    ans = []
    for i in range(size):
        for j in range(size):
            if inp[i][j] == 0:
                #fill here
                poss = calc(inp,i,j)
                if poss == []:
                    return []
                for k in poss:
                    inp1 = [[y for y in x] for x in inp]
                    inp1[i][j] = k
                    ans = solve(inp1,start,delay_time)
                    if ans:
                        return ans
                found = 1
                break
        if found == 1:
            break
    return []






