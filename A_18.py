# Greedy algorithms(code):

# Code --- >
# buildings = {
# 'B81':{16,17,18},
# 'B02':{1,11,4,30},
# 'B03':{17,18,27,30},
# 'B84':{1,7,17,19,30},
# 'B05':{7,11,15,17,20},
# 'B06':{11,6,7},
# 'B07':{30,23},
# 'B08':{10,14,18,25,29},
# 'B09':{16,17,18,19},
# 'B10':{10,19,13},
# 'B11':{1,3,6,13,16},
# 'B12':{8,12},
# 'B13':{10,5,15},
# 'B14':{5,8,17,23,24},
# 'B15':{2,9,21,22,26,28},
# }
# regions = {
#   1,2,3,4,5,6,7,8,9,10,
#   11,12,13,14,15,16,17,18,19,20,
#   21,22,23,24,25,26,27,28,29,30,
# }

# final_buildings = set()
# while regions:
#     best_building = None
#     covered_areas = set()
#     for building, building_scope in buildings.items():
#         coverage = regions & building_scope
#         print(f"{building}:{coverage}")
#         if len(coverage) > len(covered_areas):
#             best_building = building
#             covered_areas = coverage
#     regions -= covered_areas
#     final_buildings.add(best_building)
#     print(f"Selected building: {best_building}")
#     print(f"Remaining areas: {regions}")
#     print(f"Selected recent buildings: {final_buildings}")
#     input()
# Traveling Salesperson(en):
# The travelling salesperson problem (TSP) is a classic optimization problem where the goal is to determine the shortest tour of a collection of n “cities” (i.e. nodes), starting and ending in the same city and visiting all of the other cities exactly once.

# Traveling Salesperson(ru):
# Задача коммивояжера (TSP) — это классическая задача оптимизации, целью которой является определение кратчайшего пути по набору из n «городов» (т. е. узлов), начинающихся и заканчивающихся в одном и том же городе и посещающих все остальные города ровно один раз.

# Big_O:
# For Traveling Salesperson: O(n!)

# Combination formula:
# Формула комбинации:
# n! = 1 *...* n 
# Ex:4! = 1 * 2 * 3 * 4 = 24

# Code --- >

from sys import maxsize
from itertools import permutations

# implementation of traveling Salesman Problem
# реализация задачи коммивояжера
def travellingSalesmanProblem(graph, s):

	# store all Node apart from source Node
  # сохранить все вершины, кроме исходной вершины
	Node = []
	for i in range(4):
		if i != s:
			Node.append(i)

	# store minimum weight Hamiltonian Cycle
  # сохранить минимальный вес гамильтонового цикла
	min_path = maxsize
	next_permutation = permutations(Node)
	for i in next_permutation:

		# store current Path weight(cost)
    # сохранить текущий вес пути (стоимость)
		current_pathweight = 0

		# compute current path weight
    # вычислить текущий вес пути
		k = s
		for j in i:
			current_pathweight += graph[k][j]
			k = j
		current_pathweight += graph[k][s]

		# update minimum
    # обновить минимум
		min_path = min(min_path, current_pathweight)
		
	return min_path


# Driver Code
# Код драйвера
if __name__ == "__main__":

	# Matrix representation of graph
  # Матричное представление графа
	graph = [[0, 10, 15, 20], [10, 0, 35, 25],
			[15, 35, 0, 30], [20, 25, 30, 0]]
	s = 0
	print(travellingSalesmanProblem(graph, s))
