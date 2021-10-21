def sortArray():
    randomArray = input("Type your chosen numbers: ")
    randArrSpl = randomArray.split(", ")
    arrInt = map(int, randArrSpl)
    return(sorted(arrInt)[0])

# print(sortArray())

def countingSort(arr):
    n = len(arr)
    arr1 = [0] * n

    x = [0] * 10

    for i in range(0, n):
        x[arr[i]] += 1

    for i in range(1, 10):
        x[i] += x[i - 1]


    i = n - 1
    while i >= 0:
        arr1[x[arr[i]] - 1] = arr[i]
        x[arr[i]] -= 1
        i -= 1

    for i in range(0, n):
        arr[i] = arr1[i]


arr = [4, 2, 2, 8, 3, 3, 1]

def fibSeq(n):
    # n = 100
    n1, n2 = 0, 1
    count = 0

    if n < 0:
        while count > n:
            print(n1)
            nth = n1 - n2
            n1 = n2
            n2 = nth
            count -= 1
    elif n >= 0:
        while count < n:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

fibSeq(n = int(input("Fibonacci sequence up to?: ")))