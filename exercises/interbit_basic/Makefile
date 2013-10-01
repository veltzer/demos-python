.PHONY: all
all:
	$(info please tell me what to make...)

.PHONY: clean_compiled
clean_compiled:
	-@rm -f `find . -type f -and \( -name "*.pyo" -or -name "*.pyc" \)`
.PHONY: show_compiled
show_compiled:
	@find . -type f -and -name "*.pyp" -and -name "*.pyc"
.PHONY: show_extra
show_extra:
	@find . -type f -and -not -name "*.py" -and -not -name "Makefile"
