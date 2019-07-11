# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Student:
    def __init__(self, name, surname, class_room, subject, mother, father):
        self.name = name,
        self.surname = surname
        self.class_room = class_room
        self.subject = subject
        self.mother = mother
        self.father = father

    @property
    def class_rooms(self):
        return self.clss_room

    @property
    def parents(self):
        return {'mother': self.mother,
                'father': self.father}


class Teacher:
    def __init__(self,name, surname, subject, class_room):
        self.name = name
        self.surname = surname
        self.subject = subject
        self.class_room = class_room

    @property
    def subjects(self):
        return self.subject

class Classes:
    def __init__(self,teachers, students, subjects):
        self.teachers = teachers
        self.student = students
        self.subjects = subjects

    def 

