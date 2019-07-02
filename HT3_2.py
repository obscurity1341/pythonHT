# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    f = [1, 1]
    a1 = 1
    a2 = 1
    for i in range(m):
        a1, a2 = a2, a1+a2
        f.append(a1)& f.append(a2)
        i++
        return f[n:m]
    pass


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    a = len(origin_list) -1
    b = 1
    while (b < a):
        for i in range (a - i):
            if origin_list[j-1] > origin_list [j]:
                origin_list[j-1], origin_list[j] = origin_list[j], origin_list[j-1]+origin_list[j]
            i+=1

        return origin_list
    pass


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

[i for i in list if i > N]

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.