def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    print(insertion_sort([1, 2, 3, 4, 5, 6]))
    print(insertion_sort([6, 5, 4, 3, 2, 1]))
    print(insertion_sort([6, 1, 3, 2, 4, 5]))

