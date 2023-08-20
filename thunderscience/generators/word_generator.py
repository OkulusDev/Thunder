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
from random import choice


class WordGenerator:
	def __init__(self, lang):
		self.lang = lang
		self.words = {
			'en': ['hello', 'world', 'milk', 'bread', 'tea', 'coffee', 'license',
			'program', 'this', 'there', 'software', 'hardware', 'butter', 'algorithm',
			'algorithms', 'copyright', 'world', 'fitness', 'version', 'warranty',
			'public', 'details', 'copy', 'detail', 'clear', 'english', 'russian', 'spain',
			'hole', 'hope', 'more', 'see', 'water', 'mustaches', 'beard', 'bear',
			'wolf', 'cow', 'pig', 'chicken', 'sparrow', 'arrow', 'look', 'sea',
			'ocean', 'ship', 'space', 'ignore', 'effect', 'main', 'require', 'requirement',
			'sort', 'bubble', 'node', 'word', 'generator', 'dict', 'dictionary',
			'list', 'string', 'integer', 'digit', 'boolean', 'text', 'document',
			'purprose', 'general', 'that', 'useful', 'with', 'without', 'but', 'will',
			'along', 'alone', 'hacker', 'coder', 'programmer', 'option', 'free',
			'foundation', 'terms', 'coding', 'thunder', 'science', 'eye', 'mouth',
			'shoulder', 'shoes', 'shoulders', 'oblivion', 'eat', 'bee', 'worm',
			'cold', 'rain', 'storm', 'sun', 'cloud', 'online', 'offline', 'processor',
			'memory'],
			'ru': ['привет', 'мир']
		}

	def get_word(self) -> str:
		return choice(self.words[self.lang])
