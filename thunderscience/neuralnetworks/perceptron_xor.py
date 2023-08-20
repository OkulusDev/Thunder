#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Thunder AI - проект для анализа данных, машинного обучения и искусственного интеллекта
Персептрон (нейронная сеть) без поддержки задачи XOR
Язык программирования: Python 3
Создатель: Okulus Dev (C) 2023
Лицензия: GNU GPL v3"""
import numpy as np
import matplotlib as plt


def act(x: float) -> int:
	"""Вспомогательная функция активации нейронной сети
	Возвращаем 0 если x меньше или равно 0, и 1 во всех остальные случаях

	Аргументы:
	 + x: float - переменная x

	Возвращает:
	 + int - 0 или 1"""
	return 0 if x <= 0 else 1


def perceptron_xor_neural_network(C):
	x = np.array([C[0], C[1], 1])
	w1 = [1, 1, -1.5]
	w2 = [1, 1, -0.5]
	w_hidden = np.array([w1, w2])
	w_out = np.array([-1, 1, -0.5])

	sum = np.dot(w_hidden, x)
	out = [act(x) for x in sum]
	out.append(1)
	out = np.array(out)

	sum = np.dot(w_out, out)
	y = act(sum)

	return y


def perceptron_xor():
	C1 = [(1, 0), (0, 1)]
	C2 = [(0, 0), (1, 1)]

	print(perceptron_xor_neural_network(C1[0]), perceptron_xor_neural_network(C1[1]))
	print(perceptron_xor_neural_network(C2[0]), perceptron_xor_neural_network(C2[1]))
