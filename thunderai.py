#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Thunder AI - проект для анализа данных, машинного обучения и искусственного интеллекта
Язык программирования: Python 3
Создатель: Okulus Dev (C) 2023
Лицензия: GNU GPL v3"""
from thunderscience.parser import Parser
from thunderscience.neuralnetworks.futurized import is_futurized
from thunderscience.neuralnetworks.perceptron import perceptron
from thunderscience.neuralnetworks.perceptron_xor import perceptron_xor

logo = '''           $$$$$$"
          3$$$$$"
         z$$$$P
        d$$$$"          __  __                    __                    _ 
      .$$$$$"          / /_/ /_  __  ______  ____/ /__  _____    ____ _(_)
     z$$$$$"          / __/ __ \\/ / / / __ \\/ __  / _ \\/ ___/   / __ `/ / 
   d$$$$$$$$$$"      / /_/ / / / /_/ / / / / /_/ /  __/ /      / /_/ / / 
  *******$$$"        \\__/_/ /_/\\__,_/_/ /_/\\__,_/\\___/_/   (_) \\__,_/_/ 
       .$$$"        
      .$$"
     4$P"
    z$"
   z'''

futurized_help = '''Futurized - полносвязная нейронная сеть. 
Данная нейронная сеть узнает, являешься ли ты человеком будущего или нет. 
Чтобы протестировать эту нейронную сеть, вам нужно ввести ваши интересы:
thunderai.py --futurized <Наличие гаджета> <пишите ли вы только на бумаге> <Интерес к технологиям>. 
Пример - thunderai.py --futurized "1 1 1" (интерес есть, знание есть, гаджет есть). 
Разделяйте пробелом интересы по порядку, где 0 - ложь, где 1 - истина'''
perceptron_help = '''Нейронная сеть персептрона. Чтобы показать на графике, используйте как аргумент "show": thunderai.py --perceptron show'''


def main():
	print(logo)
	parser = Parser('[󱐋] Thunder AI - проект для анализа данных, машинного обучения и искусственного интеллекта')

	parser.add_argument('--futurized', futurized_help)
	parser.add_argument('--perceptron', perceptron_help)
	args = parser.get_args()

	if args.futurized:
		futurized_params = str(args.futurized).split(" ")

		if len(futurized_params) == 3:
			for i in futurized_params:
				if str(i) == '0' or str(i) == '1' and int(i):
					continue
				else:
					print('Пожалуйста, не используйте значения, не равные 0 и 1')
					exit()
		else:
			print('Количество параметров должно быть равно 3')
			exit()

		if is_futurized(int(futurized_params[0]), int(futurized_params[1]), int(futurized_params[2])):
			print('[󱐋 Thunder.AI] Вы являетесь человеком будущего!')
		else:
			print('[󱐋 Thunder.AI] Вы не являетесь человеком будущего.')
	elif args.perceptron:
		print('[󱐋 Thunder.AI] Perceptron XOR')
		perceptron_xor()

		if str(args.perceptron).lower() == 'show':
			print('[󱐋 Thunder.AI] Ожидание создания персептрона и графика...')
			perceptron(True)
		else:
			print('[󱐋 Thunder.AI] Ожидание создания персептрона...')
			perceptron(False)

	return


if __name__ == '__main__':
	main()
