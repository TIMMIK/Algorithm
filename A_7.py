# Recursion(en):
# Python also allows function recursion, which means that a certain function can call itself. 
# Recursion is a general mathematical and programming concept. This means that the function calls itself. 
# The advantage of this is that you can iterate over the data to achieve the result.

# Recursion(ru):
# Python также допускает рекурсию функций, что означает, что определенная функция может вызывать сама себя.
# Рекурсия — это общая концепция математики и программирования. Это означает, что функция вызывает сама себя.
# Преимущество этого в том, что вы можете перебирать данные для достижения результата.

# Code(1) --- >
# def i(n):
#   print(n)
#   if n <= 1:
#     return
#   else:
#     i(n - 1)
# i(10)
# Code(2) --- >
def fact(x):
  print(x, end = ' ')
  if x == 1:
    return 1
  else:
    return x * fact(x-1)
print(fact(5))
