#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Thunder AI - проект для анализа данных, машинного обучения и искусственного интеллекта
Полносвязная нейронная сеть
Язык программирования: Python 3
Создатель: Okulus Dev (C) 2023
Лицензия: GNU GPL v3"""
import numpy as np


def act(x: float) -> int:
	"""Вспомогательная функция активации нейронной сети
	Возвращаем 0 если x меньше 0.5, и 1 во всех остальные случаях

	Аргументы:
	 + x: float - переменная x

	Возвращает:
	 + int - 0 или 1"""
	return 0 if x < 0.5 else 1


def neural_network_futurized(have_computer: int, old_write: int, techno: int) -> int:
	"""Функция полносвязной нейронной сети для определения современного человека

	Аргументы:
	 + have_computer: int - есть ли компьютер (0 или 1)
	 + techno: int - интерес к технологиям (0 или 1)
	 + old_write: int - только использование бумаги для записей (0 или 1)

	Возвращает:
	 + have_computer: int - 0 или 1, современный или консервативный человек"""
	x = np.array([have_computer, old_write, techno])
	w11 = [0.3, 0.3, 0]
	w12 = [0.4, -0.5, 1]

	weight1 = np.array([w11, w12]) 				# Матрица 2x3
	weight2 = np.array([-1, 1])					# Вектор 1x3

	sum_hidden = np.dot(weight1, x)
	print(f'[󱐋 Thunder.AI] Значение сумм на нейронах скрытого слоя: {sum_hidden}')

	out_hidden = np.array([act(x) for x in sum_hidden])
	print(f'[󱐋 Thunder.AI] Значения на выходах нейронов скрытого слоя: {out_hidden}')

	sum_end = np.dot(weight2, out_hidden)
	y = act(sum_end)
	#print(f'Выходное значение НС: {y}')

	return y


def is_futurized(techno: int, old_write: int, have_computer: int) -> bool:
	result = neural_network_futurized(techno, old_write, have_computer)

	if result == 1:
		return True
	else:
		return False
