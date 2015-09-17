.PHONY: all
all: embed

PYTHON_CFLAGS:=$(shell python-config --cflags)
PYTHON_LIBS:=$(shell python-config --libs)

embed: embed.c
	gcc -o $@ $< $(PYTHON_CFLAGS) $(PYTHON_LIBS)

.PHONY: clean
clean:
	-rm -f embed

.PHONY: debug
debug:
	$(info PYTHON_CFLAGS is $(PYTHON_CFLAGS))
	$(info PYTHON_LIBS is $(PYTHON_LIBS))
