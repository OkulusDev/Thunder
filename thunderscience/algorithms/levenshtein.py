#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""ThunderScience - библиотека для алгоритмов, обработки данных, математики, науки, машинного обучения и криптографии
levenshtein.py - алгоритм неточного сравнения строк Левенштейна
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


def distance(str1: str, str2: str) -> int:
	def rec(i, j):
		if i == 0 or j == 0:
			return max(i, j)
		elif str1[i - 1] == str2[j-1]:
			return rec(i-1, j-1)
		else:
			return 1 + min(
				rec(i, j-1),
				rec(i-1, j),
				rec(i-1, j-1)
			)

	return rec(len(str1), len(str2))


def percent_distance(distance: int, str1: str, str2: str) -> float:
	bigger = max([len(str1), len(str2)])
	perc = ((bigger - distance) / bigger) * 100

	return float(perc)
