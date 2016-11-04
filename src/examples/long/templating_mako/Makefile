.PHONY: all
all: simple.out
	$(info doing [$@])

simple.out: simple.mako mako_wrapper.py
	$(info doing [$@])
	@./mako_wrapper.py $< $@

.PHONY: clean
clean:
	$(info doing [$@])
	@-rm -f *.out
