# Merge Sort(en):
# Merge Sort is a Divide and Conquer algorithm. 
# It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. 
# The merge() function is used for merging two halves.

# Merge Sort(ru):
# Сортировка слиянием — это алгоритм «разделяй и властвуй». 
# Он делит входной массив на две половины, вызывает себя для двух половин, а затем объединяет две отсортированные половины. 
# Функция merge() используется для слияния двух половин.

# Code --- >
def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        # Рекурсивный вызов каждой половины
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        # Два итератора для обхода двух половин
        i = 0
        j = 0
        
        # Iterator for the main list
        # Итератор для основного списка
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              # Было использовано значение из левой половины
              myList[k] = left[i]
              # Move the iterator forward
              # Переместить итератор вперед
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            # Перейти к следующему слоту
            k += 1

        # For all the remaining values
        # Для всех остальных значений
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = [54,26,93,17,77,31,44,55,20]
mergeSort(myList)
print(myList)