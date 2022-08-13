# Quick Sort(en):
# Quick Sort is a divide and conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot. 
# There are many different versions of quickSort that pick pivot in different ways.

# Quick Sort(ru):
# Quick Sort — это алгоритм «разделяй и властвуй». Он выбирает элемент в качестве опорного элемента и разбивает заданный массив вокруг выбранного опорного элемента.
# Существует много разных версий quickSort, которые по-разному выбирают точку опоры.

# Code --- >

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot

        # Если текущее значение, на которое мы смотрим, больше, чем точка поворота
         # он в нужном месте (справа от точки поворота), и мы можем двигаться влево,
         # к следующему элементу.
         # Нам также нужно убедиться, что мы не превзошли нижний указатель, так как
         # указывает, что мы уже переместили все элементы на правильную сторону от оси
        while low <= high and array[high] >= pivot:
            high -= 1

        # Opposite process of the one above
        # Процесс, противоположный предыдущему
        while low <= high and array[low] <= pivot:
            low += 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop

        # Мы либо нашли значения как для максимума, так и для минимума, которые не соответствуют порядку
         # или low выше high, в этом случае выходим из цикла
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return
    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
array = [29,99,12,21,44]
quick_sort(array, 0, len(array) - 1)
print(array)