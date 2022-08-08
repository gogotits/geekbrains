print('Задание № 1')

list = [3, 3.0, 'валера']
print(type(list[0]))
print(type(list[1]))
print(type(list[2]))

print('Задание № 2')

my_list = []
i = 0
border = int(input('Сколько чисел Вы хотите добавить в список? '))
while i < int(border):
    numbers = input(f'Давайте добавим {i + 1} чиcло ')
    my_list.append(numbers)
    i += 1
n = 0
leng = len(my_list)
p = my_list[n:n+2]
print(p.reverse())
new_list = []
while n < leng:
    i = my_list[n:n+2]
    i.reverse()
    new_list.append(i)
    n += 2
print(new_list)

print('Задание № 3')

month = input('Введите номер месяца от 1 до 12: ')
decades_list = ['зимним', 'весенним', 'летним', 'осенним']
months_dict = {
    '1': 'Январь',
    '2': 'Февраль',
    '3': 'Март',
    '4': 'Апрель',
    '5': 'Май',
    '6': 'Июнь',
    '7': 'Июль',
    '8': 'Август',
    '9': 'Сентябрь',
    '10': 'Октябрь',
    '11': 'Ноябрь',
    '12': 'Декабрь'
}
if month == '12' or month <= '2':
    print(f'{month} месяц - это {months_dict[month]}. Этот месяц является {decades_list[0]} временем года')
elif '2' < month <= '5':
    print(f'{month} месяц - это {months_dict[month]}. Этот месяц является {decades_list[1]} временем года')
elif '5' < month <= '8':
    print(f'{month} месяц - это {months_dict[month]}. Этот месяц является {decades_list[2]} временем года')
elif '8' < month <= '11':
    print(f'{month} месяц - это {months_dict[month]}. Этот месяц является {decades_list[3]} временем года')

print('Задание №4')

frazy = input('Введите строку: ')
razdel_frazy = frazy.split()
list_razdel_frazy = list(razdel_frazy)
n = 0

for fraza in list_razdel_frazy:
    frazy [n]
    n += 1
    print(f'\n{n} слово {fraza[:10]}')

print('Задание №5')

n = 0
my_list = [1, 2, 4, 5, 7]

def fun_1():
    if n == 0:
        t = 0
        while len(my_list) <= 10:
            i = int(input('Введите число, а когда надоест введите "1000": '))
            my_list.append(i)
            my_list.sort()
            my_list.reverse()
            print(my_list)
            t += 1
        # elif i == 1000:
        #     print(f'спасибо, вот что получилось {my_list}') Не понимаю, как завершить цикл, чтобы он не был бесконечным.

fun_1()
print('Больше 10 числе нельзя')


print('Задание №6')



