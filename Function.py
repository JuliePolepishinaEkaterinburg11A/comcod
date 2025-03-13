list = input("введите список, значения вводите через запятую, без пробелов: ").split(',')

for i in list:
  try:
    if int(i) == float(i):
      if list.count(i) % 2:
        print(i)
  except:
    pass
