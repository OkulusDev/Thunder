RES_DIR=res
PYTHON=python3
PIP=pip3
REQ_PIP=requirements.txt
MAINFILE=thunderai.py
CC=gcc

MD5HASH_SRC=thunderscience/hash/src/md5hash.cpp
MD5HASH_BIN=thunderscience/hash/md5hash

run:
	$(PYTHON) $(MAINFILE) --help

build:
	$(PIP) install -r $(REQ_PIP)
	$(CC) $(MD5HASH_SRC) -o $(MD5HASH_BIN)
	

install:
	$(PIP) install -r $(REQ_PIP)
