n = int(input())
li = []
for i in range(n):
    temp = list(map(int,input().split()))
    li.append(temp)

answer = 0
for i in range(n-2):
    for j in range(n-2):
        temp = 0
        for row in li[i:i+3]:
            temp += sum(row[j:j+3])
        answer = max(answer,temp)

print(answer)