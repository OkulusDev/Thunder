#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Thunder AI - проект для анализа данных, машинного обучения и искусственного интеллекта
Язык программирования: Python 3
Создатель: Okulus Dev (C) 2023
Лицензия: GNU GPL v3"""
from thunderlibs import Parser

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

analyzedata_help = '''Анализ одного из доступных датасетов:
prolangperc - популярность языков программирования с 2004 до 2023
proglangfull - полная информация про популярность языков
ufosightings - информация о наблюдениях НЛО'''


def main():
	print(logo)
	parser = Parser('[󱐋] Thunder AI - проект для анализа данных, машинного обучения и искусственного интеллекта')

	parser.add_argument('--analyzedata', analyzedata_help)
	args = parser.get_args()

	if args.analyzedata:
		if args.analyzedata == 'proglangperc':
			print('[!] К сожалению, эта функция в разработке!')
		elif args.analyzedata == 'proglangfull':
			print('[!] К сожалению, эта функция в разработке!')
		elif args.analyzedata == 'ufosightings':
			print('[!] К сожалению, эта функция в разработке!')
		else:
			print('[!] Данный датасет не найден. Используйте один из следующих: proglangperc; proglangfull; ufosightings')
	else:
		print(args.analyzedata)


if __name__ == '__main__':
	main()
