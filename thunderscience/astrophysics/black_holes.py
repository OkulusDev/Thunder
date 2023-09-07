#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Thunder AI - проект для анализа данных, машинного обучения и искусственного интеллекта
Язык программирования: Python 3
Создатель: Okulus Dev (C) 2023
Лицензия: GNU GPL v3"""
import numpy as np
import matplotlib.pyplot as plt


def show_black_hole_graphic():
	# Параметры черной дыры
	M_bh = 1.989e30 * 10  # Масса черной дыры (10 солнечных масс)
	r_schwarzchild = (2 * 6.67430e-11 * M_bh) / (3e8)**2  # Радиус Шварцшильда

	# Расчет орбиты частицы вокруг черной дыры
	def calculate_orbit(initial_distance, initial_velocity, time_step, total_time):
		r = initial_distance
		v = initial_velocity
		time_points = []
		distances = []

		for t in np.arange(0, total_time, time_step):
			a = -(6.67430e-11 * M_bh) / r**2
			v += a * time_step
			r += v * time_step
			time_points.append(t)
			distances.append(r)

		return time_points, distances

	# Исследование орбиты частицы
	initial_distance = 1.5 * r_schwarzchild  # Начальное расстояние от центра черной дыры
	initial_velocity = 0.9 * (2 * 6.67430e-11 * M_bh / initial_distance)**0.5  # Начальная скорость
	time_step = 1  # Шаг интеграции
	total_time = 1000  # Время моделирования

	time_points, distances = calculate_orbit(initial_distance, initial_velocity, time_step, total_time)

	# Визуализация орбиты
	plt.plot(time_points, distances)
	plt.xlabel("Время (секунды)")
	plt.ylabel("Расстояние от черной дыры (метры)")
	plt.title("Моделирование орбиты частицы вокруг черной дыры")
	plt.grid(True)
	plt.show()
	