def findSmallest(array: list[int]) -> int:
    smallest: int = array[0]
    smallest_index = 0
    length_of_array: int = len(array)
    for i in range(1, length_of_array):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selectionSort(array: list[int]) -> list[int]:
    new_array: list[int] = []
    length_of_array: int = len(array)
    for i in range(length_of_array):
        smallest: int = findSmallest(array)
        new_array.append(array.pop(smallest))
    return new_array

def main() -> None:
    array: list[int] = [2, 3, 9, 1, 10, 4, 15, 5, 8, 6, 7]
    print(f"Original array: {array}")
    sorted_array: list[int] = selectionSort(array)
    print(f"Sorted array: {sorted_array}")
    
if __name__ == "__main__":
    main()