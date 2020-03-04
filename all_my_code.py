def print_hello_world():
	print('Приветствую!')


def admin_username_pswd():
	admin_name = 'admin'
	admin_pswd = 'admin'
	while True:
		name = input('Введите имя администратора: ')
		pswd = input('Введите пароль администратора: ')
		if name != admin_name:
			print(f'{name}, не является администратором.')
			continue
		elif pswd != admin_pswd and name == admin_name:
			print(f'{name}, вы ввели неверный пароль')
			continue
		else:
			print(f'{name}, добро пожаловать!')
			break



def list_compreherson():
	foo = input('Введите что хотите, я сделаю список: ')
	bar = [baz for baz in foo]
	print(bar)



def e_numerate():
	user_input = input('Введите слово которое хотите пронумеровать: ')
	for index, letter in enumerate(user_input):
		print(letter + ' is at index ' + str(index))


def maxmin():
	maxmin = input('Найти min() и max(): ')
	foo = maxmin
	print(f'Минимальное значение введенного равна {min(foo)}.')
	print(f'Максимальное значение введенного равна {max(foo)}.')



def sum_of_two_numbers(foo=0, bar=0):
	return foo+bar
baz = (sum_of_two_numbers(1, 2)) 	
print(f'{baz} посмотри на 44 строку')


def ten_percent_with_args(*args):
	foo = int(input('Введите число и я верну 10% от вашего числа: '))
	for bar in args:
		foo = foo * bar
	print("10% от вашего числа равна: ", foo * 0.1)


print_hello_world()
admin_username_pswd()
list_compreherson()
e_numerate()
maxmin()
ten_percent_with_args()