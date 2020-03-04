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
	x = input('Введите что хотите, я сделаю список: ')
	y = [z for z in x]
	print(y)



def e_numerate():
	user_input = input('Введите слово которое хотите пронумеровать: ')
	for index, letter in enumerate(user_input):
		print(letter + ' is at index ' + str(index))


def maxmin():
	maxmin = input('Найти min() и max(): ')
	x = maxmin
	print(f'Минимальное значение введенного равна {min(x)}.')
	print(f'Максимальное значение введенного равна {max(x)}.')






admin_username_pswd()
list_compreherson()
e_numerate()
maxmin()
