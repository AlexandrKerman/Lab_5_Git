# [127] В данном массиве замените все нулевые элементы наи¬большим элементом.

import numpy as np

# Вычисление варианта (мне лень самому считать)
def variant ():
    Student = {
        "Group": 13,
        "Num": 7
    }
    N = ((Student["Group"]-1)*10+Student["Num"])%187
    print (f"Вариант: {N}\n")

def main ():
    rand_array = np.array ([2, 5, None, 5, 1, 9, 0, None, 4, None]);
    print (f"Исходный массив: {rand_array}")
    rand_array_max = rand_array[0]
    for i in rand_array:
        if i is None:
            continue
        if i>rand_array_max:
            rand_array_max = i
    print (f"Максимум в нём: {rand_array_max}")
    for i in range (0, len(rand_array)):
        if rand_array[i] is None:
            print (f"rand_array[{i}] - Тут есть None")
            rand_array[i] = rand_array_max
    print (f"Массив после фильтрации: {rand_array}")



if __name__ == "__main__":
    variant()
    main ()