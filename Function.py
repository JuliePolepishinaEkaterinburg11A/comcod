list = input("введите список, значения вводите через запятую, без пробелов: ").split(',')
numbers = []
for i in list:
  try:
    if int(i) == float(i):
      if list.count(i) % 2 and !(i in list):
        list.append(i)
  except:
    pass
print(numbers)
