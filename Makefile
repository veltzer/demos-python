.PHONY: all
all:
	$(info please tell me what to make...)

.PHONY: check_all
check_all: check_doublespace check_endspace check_eq check_eqq

.PHONY: check_doublespace
check_doublespace:
	$(info doing $@)
	@-git grep -e "  " -- \*.py
.PHONY: check_endspace
check_endspace:
	$(info doing $@)
	@-git grep -e "\s$$" -- \*.py
.PHONY: check_eq
check_eq:
	$(info doing $@)
	@-git grep -e " = " -- \*.py
.PHONY: check_eqq
check_eqq:
	$(info doing $@)
	@-git grep -e " == " -- \*.py
	@-git grep -e " != " -- \*.py
	@-git grep -e " < " -- \*.py
	@-git grep -e " > " -- \*.py
	@-git grep -e " % " -- \*.py
	@-git grep -e " / " -- \*.py
	@-git grep -e " + " -- \*.py
	@-git grep -e " - " -- \*.py
	@-git grep -e " <= " -- \*.py
	@-git grep -e " => " -- \*.py
.PHONY: check_syn
check_syn:
	-git grep ";"
	-git grep " = "
	-git grep " \","
	-git grep ", "
	-git grep "print\ "
	-git grep --files-without-match "mark@veltzer.net"
.PHONY: clean_compiled
clean_compiled:
	-@rm -f `find . -type f -and \( -name "*.pyo" -or -name "*.pyc" \)`
.PHONY: show_compiled
show_compiled:
	@find . -type f -and -name "*.pyp" -and -name "*.pyc"
.PHONY: show_extra
show_extra:
	@find . -type f -and -not -name "*.py" -and -not -name "Makefile"
