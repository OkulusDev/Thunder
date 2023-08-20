#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Thunder AI - проект для анализа данных, машинного обучения и искусственного интеллекта
Персептрон (нейронная сеть) без поддержки задачи XOR
Язык программирования: Python 3
Создатель: Okulus Dev (C) 2023
Лицензия: GNU GPL v3"""
import numpy as np
import matplotlib.pyplot as plt


def perceptron(show_graphic: bool):
	N = 5
	b = 3

	x1 = np.random.random(N)
	x2 = x1 + [np.random.randint(10) / 10 for i in range(N)] + b
	C1 = [x1, x2]

	x1 = np.random.random(N)
	x2 = x1 - [np.random.randint(10) / 10 for i in range(N)] - 0.1 + b
	C2 = [x1, x2]

	f = [0 + b, 1 + b]

	w2 = 0.5
	w3 = -b * w2
	w = np.array([-w2, w2, w3])

	for i in range(N):
		x = np.array([C1[0][i], C1[1][i], 1])
		y = np.dot(w, x)

		if y >= 0:
			print('[󱐋 Thunder.AI] Class C1')
		else:
			print('[󱐋 Thunder.AI] Class C2')

	if show_graphic:
		plt.scatter(C1[0][:], C1[1][:], s=10, c='magenta')
		plt.scatter(C2[0][:], C2[1][:], s=10, c='red')
		plt.plot(f)
		plt.grid(True)
		plt.show()
