def selection_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


if __name__ == "__main__":
    ls = [6, 5, 4, 3, 2, 1]
    print(selection_sort(ls))
    ls = [6, 4, 5, 3, 1, 2]
    print(selection_sort(ls))
    ls = [1, 2, 3, 4, 5, 6]
    print(selection_sort(ls))
