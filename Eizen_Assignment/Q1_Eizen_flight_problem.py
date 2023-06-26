
ls = list(map(int, input().split()))

n,m = ls[0],ls[1]

group = list(map(int, input().split()))
planes = list(map(int, input().split()))

group.sort(reverse=True)
planes.sort(reverse=True)

if(group[0]>planes[0]):
    print(-1)
    exit()

i = 0
j = 0

total_time = 0
turn = 0
return_back = 0
while(i<n):
    if(j == m):
        j = 0
        turn = 0
        return_back = 1
    if(group[i]>planes[j]):
        turn = 0
        j = 0
        return_back = 1
    else:
        if(turn == 0):
            total_time += 1
            turn = 1
        if(return_back == 1):
            total_time += 1
            return_back = 0
        i += 1
        j += 1

print(total_time)