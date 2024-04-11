n,m = map(int,input().split())
li = [list(map(int, input().split())) for _ in range(n)]

happy_count = 0

for i in li:
    continue_num = 0
    count = 1
    high = 1
    for j in i:
        if continue_num == 0:
            continue_num = j
        elif continue_num != j:
            continue_num = j
            count = 1
        elif continue_num == j:
            count+=1
        if high < count: 
            high = count
        if high >= m:
            happy_count+=1
            break
    
for i in range(n):
    continue_num = 0
    count = 1
    high = 1
    for j in range(n):
        now_num = li[j][i]
        if continue_num == 0:
            continue_num = now_num
        elif continue_num != now_num:
            continue_num = now_num
            count = 1
        elif continue_num == now_num:
            count+=1
        if high < count: 
            high = count
        if high > m:
            happy_count+=1
            break 

print(happy_count)