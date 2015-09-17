.PHONY: all
all: _car.so _atoi.so

_atoi.so: atoi_wrap.c
	./setup_atoi.py build

_car.so: car_wrap.cxx car.cc
	./setup_car.py build

car.py car_wrap.cxx: car.i
	swig -python -c++ car.i
atoi.py atoi_wrap.c: atoi.i
	swig -python atoi.i

.PHONY: use_car
use_car:
	./use_car.py

.PHONY: use_atoi
use_atoi:
	./use_atoi.py

.PHONY: clean
clean:
	@rm -f *_wrap.cxx *_wrap.c car.py car.pyc atoi.py atoi.pyc *.so
	@\rm -rf build
