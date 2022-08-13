# Divide & Conquer(en):
# In divide and conquer approach, the problem in hand, is divided into smaller sub-problems and then each problem is solved independently. 
# When we keep on dividing the subproblems into even smaller sub-problems, we may eventually reach a stage where no more division is possible.

# Divide & Conquer(ru):
# В подходе «разделяй и властвуй» рассматриваемая проблема делится на более мелкие подзадачи, а затем каждая проблема решается независимо. 
# Когда мы продолжаем делить подзадачи на еще более мелкие подзадачи, мы можем в конце концов достичь стадии, на которой дальнейшее разделение невозможно.

#  Code --- >
def bsearch(list, idx0, idxn, val):
   if (idxn < idx0):
      return None
   else:
      midval = idx0 + ((idxn - idx0) // 2)
   # Compare the search item with middle most value
   # Сравните элемент поиска со средним значением
   if list[midval] > val:
      return bsearch(list, idx0, midval-1,val)
   elif list[midval] < val:
      return bsearch(list, midval+1, idxn, val)
   else:
      return midval
list = [8,11,24,56,88,131]
print(bsearch(list, 0, 5, 24))
print(bsearch(list, 0, 5, 51))