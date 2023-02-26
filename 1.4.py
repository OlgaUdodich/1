a = int(input('Введіть ділене: '))
b = int(input('Введіть дільник: '))
sum_ = a
for i in range(a):
    sum_ = sum_ - b
    print(sum_)
    if sum_ <= b:
        print('Ділення завершено')
        break