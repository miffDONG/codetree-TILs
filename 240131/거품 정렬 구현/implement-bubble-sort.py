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