# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    n = int(10**(ndigits+1) * number)/ 10
    if ((n - int(n)) >= 0.5):
        return (int(n) + 1)/ 10 **(ndigits)
    else: return int(n)/10**(ndigits)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    a_numb = tuple(int(ticket_number/1000)
    for i in a_numb:
        i += i
    a_sum = i
    return a_sum
    b_numb = tuple(str(ticket_number%1000))
    for i in b_numb:
        i+=i
    b_sum = i
    return b_sum
    if (a_sum == b_sum):
        return "lucky"
    pass


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))