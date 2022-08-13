# Binary Search Tree(en):
# Binary search tree is a data structure that quickly allows us to maintain a sorted list of numbers. 
# It is called a binary tree because each tree node has a maximum of two children.

# Binary Search Tree(ru):
# Двоичное дерево поиска — это структура данных, которая позволяет нам быстро поддерживать отсортированный список чисел.
# Оно называется бинарным деревом, потому что каждый узел дерева имеет не более двух дочерних элементов.



# Code --- >

# Python program to demonstrate
# insert operation in binary search tree

# Программа Python для демонстрации
# операция вставки в бинарное дерево поиска


# A utility class that represents
# an individual node in a BST

# Вспомогательный класс, представляющий
# отдельный узел в BST

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

# A utility function to insert
# a new node with the given key

# Вспомогательная функция для вставки
# новый узел с заданным ключом

def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if root.val == key:
			return root
		elif root.val < key:
			root.right = insert(root.right, key)
		else:
			root.left = insert(root.left, key)
	return root

# A utility function to do inorder tree traversal
# Вспомогательная функция для неупорядоченного обхода дерева

def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)


# Driver program to test the above functions
# Let us create the following BST

# Программа-драйвер для проверки вышеуказанных функций
# Давайте создадим следующий BST

#        50
#      /   \
#    30	   70
#   / \   / \
# 20 40  60 80

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print inoder traversal of the BST
# Вывести иной обход BST
inorder(r)

# --------------------------------

# Inverted indexes(en):
# An inverted index is an index data structure storing a mapping from content, such as words or numbers, to its locations in a document or a set of documents. 
# In simple words, it is a hashmap like data structure that directs you from a word to a document or a web page.

# Inverted indexes(ru):
# Инвертированный индекс — это структура данных индекса, в которой хранится сопоставление содержимого, такого как слова или числа, с его расположением в документе или наборе документов. 
# Проще говоря, это хэш-карта, похожая на структуру данных, которая направляет вас от слова к документу или веб-странице.


# Furye transform(en):
# A Fourier transform (FT) is a mathematical transform that decomposes functions depending on space or time into functions depending on spatial frequency or temporal frequency. 
# That process is also called analysis.

# Furye(ru):
# Преобразование Фурье (FT) — это математическое преобразование, которое разлагает функции, зависящие от пространства или времени, на функции, зависящие от пространственной частоты или временной частоты. 
# Этот процесс также называется анализом.


# Parallel algorithm(en):
# A parallel algorithm is an algorithm that can execute several instructions simultaneously on different processing devices and then combine all the individual outputs to produce the final result.

# Parallel algorithm(ru):
# Параллельный алгоритм — это алгоритм, который может выполнять несколько инструкций одновременно на разных устройствах обработки, а затем объединять все отдельные выходные данные для получения конечного результата.

