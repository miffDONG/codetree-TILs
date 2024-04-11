import sys
sys.stdin=open('input.txt','r')

if __name__=="__main__":
    n,m=map(int,input().split())
    li = []
    happy_count = 0
    # 첫 row 입력을 받는 for문을 지나치지 않고 활용.
    for _ in range(n):
        row = list(map(int,input().split()))
        li.append(row)
        for i in range(n-m+1):
            if row[i:i+m].count(row[i]) == m:
                happy_count+=1
                break

    # zip을 통한 
    for cow in zip(*li):
        for i in range(n-m+1):
            if cow[i:i+m].count(cow[i]) == m:
                happy_count+=1
                break

    print(happy_count)