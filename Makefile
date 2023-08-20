RES_DIR=res
PYTHON=python3
PIP=pip3
REQ_PIP=requirements.txt
MAINFILE=thunderai.py

run:
	$(PYTHON) $(MAINFILE) --help

install:
	$(PIP) install -r $(REQ_PIP)
