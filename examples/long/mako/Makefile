.PHONY: all
all: simple_2.out simple_3.out
	$(info doing [$@])

simple_2.out: simple.mk mako_wrapper_2.py
	$(info doing [$@])
	@./mako_wrapper_2.py $< $@
simple_3.out: simple.mk mako_wrapper_3.py
	$(info doing [$@])
	@./mako_wrapper_3.py $< $@

.PHONY: clean
clean:
	$(info doing [$@])
	@-rm -f *.out
