list = []

def push_back(A):
    return list.append(A)

def pop_back():
    return list.pop()

def size():
    return len(list)

def get(k):
    return list[k-1]

n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == 'push_back':
        push_back(int(command[1]))

    elif command[0] == 'get':
        print(get(int(command[1])))

    elif command[0] == 'size':
        print(size())

    elif command[0] == 'pop_back':
        pop_back()