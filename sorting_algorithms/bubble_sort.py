def bubble_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - 1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    ls = [6, 5, 4, 3, 2, 1]
    print(bubble_sort(ls))
    ls = [6, 4, 5, 3, 1, 2]
    print(bubble_sort(ls))
    ls = [1, 2, 3, 4, 5, 6]
    print(bubble_sort(ls))
