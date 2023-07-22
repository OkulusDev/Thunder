#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""ThunderLibs - встроенные библиотеки Thunder AI
Язык программирования: Python 3
Создатель: Okulus Dev (C) 2023
Лицензия: GNU GPL v3"""
import argparse												# Импорт модуля argparse


class Parser:
	"""Класс парсера аргументов командной строки"""
	def __init__(self, description):
		"""Инициализация парсера аргументов командной строки"""
		self.parser = argparse.ArgumentParser(description=description)

	def add_argument(self, flag: str, help_doc: str='Для этого аргумента еще нету справки', default=None) -> None:
		self.parser.add_argument(flag, help=help_doc, default=default)

	def get_args(self):
		return self.parser.parse_args()