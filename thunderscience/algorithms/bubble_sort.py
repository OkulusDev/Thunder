#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""ThunderScience - библиотека для алгоритмов, обработки данных, математики, науки, машинного обучения и криптографии
bubble_sort.py - сортировка пузырьком
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


def bubble_sort(nums_list: list) -> list:
	"""Функция сортировки пузырьком (сортировка по возрастанию)
	Проходимся по списку и сравниваем его элементы попарно, если порядок 
	неправилен то меняем его местами

	Аргументы:
	 + nums_list: list - список для сортировки

	Возвращает:
	 + list - отсортированный список по возрастанию"""
	for i in range(len(nums_list)):
		for j in range(len(nums_list) - i - 1):
			if nums_list[j] > nums_list[j+1]:
				nums_list[j], nums_list[j+1] = nums_list[j+1], nums_list[j]

	return nums_list
