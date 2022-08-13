# Breadth-first(en):
# Breadth-first search (BFS) is an algorithm used for tree traversal on graphs or tree data structures. 
# BFS can be easily implemented using recursion and data structures like dictionaries and lists.

# Breadth-first(ru):
# Поиск в ширину (BFS) — это алгоритм, используемый для обхода дерева по графам или древовидным структурам данных. 
# BFS можно легко реализовать с помощью рекурсии и структур данных, таких как словари и списки.

# Code --- >
from collections import deque

def search(start_node, target = 'Otabek'):
   search_queue = deque()
   search_queue += graph[start_node]
   searched = set()
   
   while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person == target:
                print(f'The {target} is finded!')
                print(sorted(searched))
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
   return False

if __name__ == '__main__':
    graph = {
        'persons':['Tima','Jahon','Saidjakhon'],
        'Tima':['Asad','Mohir'],
        'Jahon':['Olim','Doston'],
        'Saidjakhon':['Islom','Otabek'],
        'Asad':[],'Mohir':[],'Olim':[],'Doston':[],'Islom':[],'Jahon':[]
    }
search('persons','Otabek')