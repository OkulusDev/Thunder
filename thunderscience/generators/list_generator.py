#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""ThunderScience - библиотека для алгоритмов, обработки данных, математики, науки, машинного обучения и криптографии
list_generator.py - генерация списка
Copyright (C) 2023  Okulus Dev
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""
from random import randint


def generate_int_list(length: int=9, min_num: int=0, max_num: int=9) -> list:
	"""Генерация списка со случайными числами

	Аргументы:
	 + length: int - длина списка (по умолчанию 9)
	 + min_num: int - минимальное число для генерации случайного числа (по умолчанию 0)
	 + max_num: int - максимальное число для генерации случайного числа (по умолчанию 9)

	Возвращает:
	 + list - список со случайными числами"""
	result = []

	for i in range(length):
		result.append(randint(min_num, max_num))

	return result
