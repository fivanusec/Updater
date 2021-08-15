PY = python3

all:
	${PY} setup.py build

install:
	sudo ${PY} setup.py install