PY = python3

all:
	${PY} setup.py build

install:
	${PY} setup.py install