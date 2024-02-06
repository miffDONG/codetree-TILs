def merge_sort(arr,low,high):
    if low < high:
        mid = (low+high) // 2
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,low,mid,high)

def merge(arr,low,mid,high):
    i , k = low , low 
    j = mid+1

    merged_arr = []

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            merged_arr.append(arr[i])
            i+=1
        else:
            merged_arr.append(arr[j])
            j+=1
        
    while i <= mid:
        merged_arr.append(arr[i])
        i+=1

    while j <= high:
        merged_arr.append(arr[j])
        j+=1

    for i in range(low,high+1):
      arr[i] = merged_arr[i-low]
    

n = int(input())
arr = list(map(int,input().split()))

merge_sort(arr,0,len(arr)-1)
for i in arr:
    print(i,end=' ')