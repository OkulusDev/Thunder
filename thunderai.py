#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Thunder AI - проект для анализа данных, машинного обучения и искусственного интеллекта
Язык программирования: Python 3
Создатель: Okulus Dev (C) 2023
Лицензия: GNU GPL v3"""
from thunderlibs import Parser


def main():
	parser = Parser('Thunder AI - проект для анализа данных, машинного обучения и искусственного интеллекта')

	args = parser.get_args()

	print(args.docs)


if __name__ == '__main__':
	main()
