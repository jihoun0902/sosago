def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = list(map(int, input("정렬할 숫자들을 입력하세요 (공백으로 구분): ").split()))
bubbleSort(arr)
print("정렬된 배열:", arr)