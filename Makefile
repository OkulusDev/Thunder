RES_DIR=res
PYTHON=python3
PIP=pip3
REQ_PIP=requirements.txt
MAINFILE=thunder.py
CC=gcc

MD5HASH_SRC=thunderscience/hash/src/md5hash.cpp

run:
	$(PYTHON) $(MAINFILE) --help

build:
	$(PIP) install -r $(REQ_PIP)

install:
	$(PIP) install -r $(REQ_PIP)
