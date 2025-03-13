list = input("введите список, значения вводите через запятую, без пробелов: ").split(',')
numbers = []
for i in list:
  try:
    if int(i) == float(i):
      if list.count(i) % 2 and !(i in numbers):
        numbers.append(i)
  except:
    pass
print(numbers)
