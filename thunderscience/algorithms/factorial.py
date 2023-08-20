#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""ThunderScience - библиотека для алгоритмов, обработки данных, математики, науки, машинного обучения и криптографии
factorial.py - вычисление факториала числа
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


def recursive_factorial(number: int) -> int:
	"""Вычисление факториала числа при помощи рекурсии
	Внимание! Если number больше тысячи, то возникнет RecursionError

	Аргументы:
	 + number: int - число для вычисления

	Возвращает:
	 + int - факториал числа"""
	if number == 0:
		return 1

	# Если number больше 1000, то возникнет ошибка переполнения стека (RecursionError)
	return recursive_factorial(number - 1) * number


def factorial(number: int) -> int:
	"""Вычисление факториала числа при помощи цикла

	Аргументы:
	 + number: int - число для вычисления

	Возвращает:
	 + int - факториал числа"""
	if number == 0:
		return 1

	factor = 1
	i = 0

	while i < number:
		i += 1
		factor = factor * i

	return factor
