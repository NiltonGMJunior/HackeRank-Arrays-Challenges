#TODO: Implement an optimal sorting algorithm that works for very large input data

def minimumSwaps(arr):
    swaps = 0
    while True:
        for i in range(len(arr) - 1):
            if arr[i + 1] < arr[i]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
        print(arr)
        if arr == arr.sort():
            return swaps

if  __name__ == "__main__":
    print(minimumSwaps([2, 3, 4, 1, 5]))
