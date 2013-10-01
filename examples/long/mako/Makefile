.PHONY: all
all: simple.out
	$(info doing [$@])

simple.out: simple.mk mako_wrapper.py
	$(info doing [$@])
	@./mako_wrapper.py $< $@

.PHONY: clean
clean:
	$(info doing [$@])
	@-rm -f simple.out
