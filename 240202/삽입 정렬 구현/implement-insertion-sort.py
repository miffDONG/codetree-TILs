def insertion_sort(arr):
    length = len(arr)
    for i in range(1,length):
        j = i-1
        key = arr[i]
        while j>=0 and arr[j] > key: # i-1번째까지 정렬 완료. i번째 단어가 들어갈 위치를 찾는 과정
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

    return arr

n = int(input())
m = list(map(int,input().split()))

sorted = insertion_sort(m)
for i in sorted:
    print(i,end=" ")