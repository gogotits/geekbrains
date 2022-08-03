print('Задание №1')

number_1 = 5
number_2 = 10

print(f'У нас есть 2 числа: первое - {number_1}; второе - {number_2}')

name = input('Привет! Как тебя зовут? ')
age = int(input(f'Очень приятно {name}! Сколько тебе лет? '))

print(f'{name}, теперь мы знакомы! Мне тоже {age} лет')


print('Задание №2')

sec = int(input('Я конвертирую секунды в формат ч/м/с. Сколько секунд конвертировать? '))

min = sec // 60
hour = sec // 3600

if sec > 0:
    sec = sec - (min * 60)
    min = min - (hour * 60)
    print(f'Конвертирование произведено. Ответ: {hour} час (ов) :{min} минут (ы) :{sec} секунд (ы)')
else:
    print('Такие числа нельзя конвертировать')

print('Задание №3')

n = input('Введите число: ')

sum = int(n) + int((n + n))  + int((n + n + n))

print(sum)

print('Задание №4')

numbers = input('Введите число: ')
i = 0
num = []
while i < len(numbers):
    number = numbers[i]
    num.append(number)
    print(f'{i+1}-e число: {number}')
    i += 1
max_num = max(num)
print(f'\nНаибольшее число: {max_num}')

print('Задание №5')

income = int(input('Значение выручки за июль: '))
opex = int(input('Значение OPEX: '))
result = income - opex


if income > opex:
    print(f'Прибыль за этот месяц составляет: {result} USD')
    profit = round(((income - opex) / income) * 100)
    print(f'Рентабельность составляет: {profit} %')
    personal = int(input('Введите количество сотрудников: '))
    profit_per_person = round(income / personal)
    print(f'Прибыль на сотрудника составляет: {profit_per_person}')
else:
    print('Этот месяц убыточный. Собираемся через 5 минут у директора')


print('Задание № 6')

n = 1
print('Давайте узнаем, через сколько дней тренировок Вы сможете пробежать нужное Вам кол-во километров')
a = int(input('Сколько килеметров Вы можете пробежать сейчас? '))
b = int(input('Сколько километров Вы хотите пробегать? '))

while a < b:
    a = float(a + (a * 0.1))
    print(f'{n}-й день: {a}')
    n += 1
if a >= b:
    print('Вы и так неплохо бегаете')
    # не могу понять как сделать условие так, чтобы выолнялось условие a > b