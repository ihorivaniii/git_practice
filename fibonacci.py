def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  fib_list = [0, 1]
  if n <= len(fib_list) - 1:
    return fib_list[n]
  else:
    while n > len(fib_list) - 1:
      sum_of_pervios_two = fib_list[-1] + fib_list[-2]
      fib_list.append(sum_of_pervios_two)
      print(fib_list)
  return fib_list[n]