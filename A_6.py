# Selction sort(en):
# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. 
# The algorithm maintains two subarrays in a given array.

# Selction sort(en):
# Алгоритм сортировки выбором сортирует массив, многократно находя минимальный элемент (с учетом возрастания) из несортированной части и помещая его в начало. 
# Алгоритм поддерживает два подмассива в заданном массиве.

# Code --- >
def selectionSort(array, size):
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            # select the minimum element in every iteration
            # выбираем минимальный элемент на каждой итерации
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
         # замена элементов для сортировки массива
        (array[i], array[min_index]) = (array[min_index], array[i])
 
arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print('Массив после сортировки по возрастанию методом выбора:')
print(arr)