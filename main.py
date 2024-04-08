def quick_sort(array: list [int]) -> list [int]:
    left = []
    right = []
    center = []
    if len(array) > 1:
        pivot = array[0]
        for i in array:
            if i > pivot:
                right.append(i)
            elif i == pivot:
                center.append(i) 
            elif i < pivot:
                left.append(i) 
        return quick_sort(left) + center + quick_sort(right)
    else:
        return array

def binary_search(array: list[int], num: int) -> int:
    low = 0 
    high = len(array) - 1
    while low <= high:
        media = (low + high) // 2
        if array[media] == num:
            return media
        elif array[media] > num:
            high = media - 1
        else:
            low = media + 1
    return -1

def main() -> None:
    arr = [5, 3, 7, 6, 2, 1, 4]
    print(quick_sort(arr))
    num = int(input('Ingrese el numero que desea buscar: '))
    if binary_search(quick_sort(arr), num) != -1:
        print(f'La posicion de tu número es: {binary_search(quick_sort(arr), num)}')
    else:
        print('No se ha encontrado el número.')

if __name__ == '__main__':
    main()