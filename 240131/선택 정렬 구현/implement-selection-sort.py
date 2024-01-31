def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        min = i
        for j in range(i+1,length):
            if arr[j] < arr[min]:
                min = j

        arr[i] , arr[min] = arr[min] , arr[i]

n = int(input())
arr = list(map(int,input().split()))

selection_sort(arr)

for i in arr:
    print(i,end=" ")