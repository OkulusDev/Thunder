#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Thunder - проект для анализа данных, машинного обучения и искусственного интеллекта
Язык программирования: Python 3
Создатель: Okulus Dev (C) 2023
Лицензия: GNU GPL v3"""
from thunderscience.parser import Parser

from thunderscience.algorithms.factorial import factorial

from thunderscience.astrophysics.planet_stars_movement import show_movement
from thunderscience.astrophysics.planet_stars_movement import show_movement_with_mars_and_gravitation
from thunderscience.astrophysics.black_holes import show_black_hole_graphic

from thunderscience.neuralnetworks.futurized import is_futurized
from thunderscience.neuralnetworks.perceptron import perceptron
from thunderscience.neuralnetworks.perceptron_xor import perceptron_xor

logo = '''           $$$$$$"
          3$$$$$"
         z$$$$P
        d$$$$"          __  __                    __
      .$$$$$"          / /_/ /_  __  ______  ____/ /__  _____
     z$$$$$"          / __/ __ \\/ / / / __ \\/ __  / _ \\/ ___/
   d$$$$$$$$$$"      / /_/ / / / /_/ / / / / /_/ /  __/ /
  *******$$$"        \\__/_/ /_/\\__,_/_/ /_/\\__,_/\\___/_/ 
       .$$$"        
      .$$"
     4$P"
    z$"
   z'''

futurized_help = '''Futurized - полносвязная нейронная сеть. 
Данная нейронная сеть узнает, являешься ли ты человеком будущего или нет. 
Чтобы протестировать эту нейронную сеть, вам нужно ввести ваши интересы:
thunder.py --futurized <Наличие гаджета> <пишите ли вы только на бумаге> <Интерес к технологиям>. 
Пример - thunder.py --futurized "1 1 1" (интерес есть, знание есть, гаджет есть). 
Разделяйте пробелом интересы по порядку, где 0 - ложь, где 1 - истина'''
perceptron_help = '''Нейронная сеть персептрона. Чтобы показать на графике, используйте как аргумент "show": thunderai.py --perceptron show'''


def main():
	print(logo)
	parser = Parser('[󱐋] Thunder - проект для анализа данных, науки, математики, хеширования, алгоритмов, машинного обучения, нейронных сетей, физики и других важных вещей.')

	parser.add_argument('--futurized', futurized_help)
	parser.add_argument('--perceptron', perceptron_help)
	parser.add_argument('--factorial', 'Факториал числа. Используйте вместе с числом.')
	parser.add_argument('--planetstars_movement', 'Используйте вместе с show, чтобы показать схему')
	parser.add_argument('--planetstars_movement_advanced', 'Используйте вместе с show, чтобы показать схему')
	parser.add_argument('--blackhole', 'Используйте вместе с show, чтобы показать график')
	args = parser.get_args()

	if args.factorial:
		if args.factorial.isdigit():
			result = factorial(args.factorial)
			print(f'Факториал числа {args.factorial} - {result}')
		else:
			print('Вы ввели не число')
	elif args.blackhole:
		if args.blackhole.lower().strip() == 'show':
			show_black_hole_graphic()
	elif args.planetstars_movement:
		if args.planetstars_movement.lower().strip() == 'show':
			show_movement()
	elif args.planetstars_movement_advanced:
		if args.planetstars_movement_advanced.lower().strip() == 'show':
			show_movement_with_mars_and_gravitation()
	elif args.futurized:
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
			print('[󱐋 Thunder] Вы являетесь человеком будущего!')
		else:
			print('[󱐋 Thunder] Вы не являетесь человеком будущего.')
	elif args.perceptron:
		print('[󱐋 Thunder] Perceptron XOR')
		perceptron_xor()

		if str(args.perceptron).lower() == 'show':
			print('[󱐋 Thunder] Ожидание создания персептрона и графика...')
			perceptron(True)
		else:
			print('[󱐋 Thunder] Ожидание создания персептрона...')
			perceptron(False)

	return


if __name__ == '__main__':
	main()
