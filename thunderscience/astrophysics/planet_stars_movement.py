#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Thunder AI - проект для анализа данных, машинного обучения и искусственного интеллекта
Язык программирования: Python 3
Создатель: Okulus Dev (C) 2023
Лицензия: GNU GPL v3"""
import numpy as np
import matplotlib.pyplot as plt


def show_movement_with_mars_and_gravitation():
	# Начальные параметры
	G = 6.67430e-11  # Гравитационная постоянная
	M_star = 1.989e30  # Масса звезды (Солнце)
	M_planet1 = 5.972e24  # Масса планеты 1 (Земля)
	M_planet2 = 6.39e23  # Масса планеты 2 (Марс)
	r_initial = 1.496e11  # Начальное расстояние от Солнца (апстрим)

	# Временные параметры
	t_max = 3.154e7 * 2  # Год в секундах (два земных года)
	dt = 3600  # Шаг интеграции (один час)

	# Инициализация массивов для хранения данных
	time_points = []
	distances_planet1 = []
	distances_planet2 = []

	# Начальные условия
	r1 = r_initial
	r2 = r_initial * 1.5  # Начальное расстояние Марса от Солнца
	v1 = 0  # Начальная скорость планеты 1
	v2 = 0  # Начальная скорость планеты 2

	# Интеграция методом Эйлера
	for t in np.arange(0, t_max, dt):
		F_gravity1 = -G * M_star * M_planet1 / r1**2
		F_gravity2 = -G * M_star * M_planet2 / r2**2
		a1 = F_gravity1 / M_planet1
		a2 = F_gravity2 / M_planet2
		v1 += a1 * dt
		v2 += a2 * dt
		r1 += v1 * dt
		r2 += v2 * dt
		time_points.append(t)
		distances_planet1.append(r1)
		distances_planet2.append(r2)

	# Визуализация
	plt.plot(time_points, distances_planet1, label="Земля")
	plt.plot(time_points, distances_planet2, label="Марс")
	plt.xlabel("Время (секунды)")
	plt.ylabel("Расстояние от Солнца (метры)")
	plt.title("Моделирование движения Земли и Марса вокруг Солнца")
	plt.legend()
	plt.grid(True)
	plt.show()


def show_movement():
	# Начальные параметры
	G = 6.67430e-11  					# Гравитационная постоянная
	M_star = 1.989e30  					# Масса звезды (Солнце)
	M_planet = 5.972e24  				# Масса планеты (Земля)
	r_initial = 1.496e11 		 		# Начальное расстояние от Солнца (апстрим)

	# Временные параметры
	t_max = 3.154e7 * 1  				# Год в секундах (один земной год)
	dt = 3600  							# Шаг интеграции (один час)

	# Инициализация массивов для хранения данных
	time_points = []
	distances = []

	# Начальные условия
	r = r_initial
	v = 0  								# Начальная скорость

	# Интеграция методом Эйлера
	for t in np.arange(0, t_max, dt):
		F_gravity = -G * M_star * M_planet / r**2
		a = F_gravity / M_planet
		v += a * dt
		r += v * dt
		time_points.append(t)
		distances.append(r)

	# Визуализация
	plt.plot(time_points, distances)
	plt.xlabel("Время (секунды)")
	plt.ylabel("Расстояние от Солнца (метры)")
	plt.title("Моделирование орбиты планеты вокруг звезды")
	plt.grid(True)
	plt.show()
