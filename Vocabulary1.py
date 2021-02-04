import json

vocabulary_book = 'Vocabulary_book.json'
vocabulary = {}
last = {}

try:
	with open(vocabulary_book, 'r') as f:
		vocabulary = json.load(f)
except FileNotFoundError:
	with open(vocabulary_book, 'w') as f:
		json.dump(vocabulary, f)

def save():
	with open(vocabulary_book, 'r') as f:
		last = json.load(f)
		if vocabulary == last :
			print('Словарь не был изменен')
			return
		
	with open(vocabulary_book, 'w') as f:
		json.dump(vocabulary, f)
		print('Словарь успешно сохранен!')
		

def add():
	print('Функции: Сбросить, Назад')
	while True:

		word = input('Слово: ')
		if word in vocabulary:
			print('\nСлово уже существует!\n')
			continue
		elif word.lower() == 'назад':
			break
		elif word.lower() == 'сбросить':
			continue

		translation = input('Перевод: ')
		if translation.lower() == 'сбросить':
			continue
		elif translation.lower() == 'назад':
			break


		vocabulary[word] =f'Перевод: {translation}'
		print('Слово успешно записано!')
		

def delete():
	while True:
		try:
			word = input('\nВведите слово, которое хотите удалить:\nФункиции: Назад\n')
			if word.lower() == 'назад':
				break
			del vocabulary[word]
			print('\nСлово успешно удалено!')
			
		except KeyError:
			print('\nЭтого слова нет в словаре.\n Проверьте правильность ввода слова\n')
			continue

def find():
	print('\nФункиции: Назад')
	while True:
		find = input('\nВведите слово или букву: \n')
		if find.lower() == 'назад':
			break
		elif len(find) == 1:
			list_keys = list(vocabulary.keys())
			list_keys.sort()
			for i in list_keys:
				if i.startswith(find):
					print(i, vocabulary[i].replace('Перевод:', '-'))	

		elif find in vocabulary:
			print(vocabulary[find])

		else:
			print('\nСлово не найдено!')
			continue	
def exit():
	with open(vocabulary_book, 'r') as f:
		last = json.load(f)
		if vocabulary == last :
			return True
		else:
			exit = input('\nСловарь был изменен. Хотите сохранить?\nДа\\Нет\n')
			if exit.lower() == 'да':
				save()
				return True
			elif exit.lower() == 'нет': 
				return True
			else:
				print('Введена не правильная команда')


while True:

		message = \
			input('\nЧто вы хотите сделать?\n Добавить, Поиск, Удалить, Сохранить, Выйти:\n ').lower()

		if message == 'добавить':
			add()		
			
		elif message == 'выйти':	
			if exit() == True:
				break
		
		elif message == 'удалить':
			delete()

		elif message == 'поиск':
			find()

		elif message == 'сохранить':
			save()	

		else:
			print('\nВведена не правильная команда!\n')	