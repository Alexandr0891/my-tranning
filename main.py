# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#######################################################################
#"Установка среды разработки PyCharm и Python."
print("Hello world")

###################################################################
# Практическое задание к уроку "Базовые структуры данных"
#"1St program"
print(9**0.5*5)
#"2nd program"
print(9.99>9.98)and(1000!=1000.1)
#"3rd program"
print(2*2+2)
print(2*(2+2))
print((2*2+2)==(2*(2+2)))
#"4th program"
'123.456'
float('123.456')
print(float('123.456'))
print(float('123.456')*10)
print(int(float('123.456')*10))
print(1234%10)










#Практическое задание по теме "Переменные"
The_number_of_completed_DZ=(12)       #Количество выполненных ДЗ
Number_of_hours_spent=(1.5)           #Количество затраченных часов
Cours_name="Python"                 #Название курса
Time_for_one_task=(Number_of_hours_spent/The_number_of_completed_DZ)    #Время на одно задание
a=Cours_name
b=The_number_of_completed_DZ
c=Number_of_hours_spent
d=Time_for_one_task
print('Курс:',a,';','всего задач:',b,';','затрачено часов:',c,';','среднее время выполнения:',d,'часа','.')

















###############################################################
#Практическое задание по уроку "Строки и индексация строк"
example="PyCharm"
print(example[0])
print(example[-1])
print(example[4:8])
print(example[::-1])
print(example[1:8:2])
#################################################









#Практическая работа по уроку "Динамическая типизация"

'module_1_3.py'
name="Alexandr"
print(name)
age=(43)
print(age)
age=(age+15)
print(age)
print(age+17)
print(age)
is_student=(True)
print(is_student)
#######################################################















#практическая работа к уроку "Организация программ и методы строк"
'module_1_4.py'

#######################################################################

#Практическое задание по теме:"Неизменяемые и изменяемые объекты. Кортежи и списки"
'module_1_5.py'
immutable_var=2,3.0,'Evpatoriya',True
print(immutable_var)
#immutable_var[0]=10   - не поддерживает назначение элементов
#print(immutable_var)     ошибка
mutable_list=[2,3.0,'Evpatoriya',True]
print(mutable_list)
mutable_list=[2,3.0,'Evpatoriya',True]
mutable_list[3]=56     #замена True на 56
print(mutable_list)

#####################################################
#Практическое задание по теме: "Словари и множества"
'module_1_6.py'
my_dict={"Александр":1980,"Василий":1982,"Павел":1979}
print(my_dict)
print(my_dict["Александр"])
my_dict["Михаил"]=2000
print(my_dict["Михаил"])
my_dict["Антон"]=2005
my_dict["Олег"]=2010
print(my_dict)
del my_dict["Михаил"]
print(my_dict.get("Михаил"))
print(my_dict)
my_set={10,2,True,"август",22,10,2,"август",22,10,2,3,5,8}  #Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
print(my_set)
my_set.add(25)      #Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.add(100)
my_set.discard(8)     #Удалите один любой элемент из множества my_set.
print(my_set)




