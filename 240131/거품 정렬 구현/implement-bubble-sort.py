# function bubble_sort(arr[])
#   set len = arr.size
#   set sorted = true
  
#   do {
#     sorted = true
#     for i = 0 ... i < len - 1
#       if a[i] > a[i + 1]
#         set tmp = a[i]
#         a[i] = a[i + 1]
#         a[i + 1] = tmp
#         sorted = false
#   } while (sorted == false)
  
#   return arr
import copy

def bubble_sort(arr):
    a = copy.deepcopy(arr)
    sorted = True
    length = len(arr)
    cycle = 1
    for i in range(length-cycle):
      if a[i] > a[i+1]:
        a[i] , a[i+1] = a[i+1] , a[i]
        sorted = False  
    cycle += 1

    while sorted == False:
      sorted = True
      for i in range(length-cycle):
        if a[i] > a[i+1]:
          a[i] , a[i+1] = a[i+1] , a[i]
          sorted = False
      cycle+=1

    return a


n = int(input())

m = list(map(int,input().split()))

bubble = bubble_sort(m)
for i in bubble:
  print(i,end=" ")