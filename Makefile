.PHONY: all
all:
	$(info please tell me what to make...)

.PHONY: check_all
check_all: check_doublespace check_endspace check_ops check_print check_endsemi check_doublequote

.PHONY: check_doublequote
check_doublequote:
	$(info doing $@)
	@-git grep \" -- \*.py
.PHONY: check_print
check_print:
	$(info doing $@)
	@-git grep -e "print " --or -e "print$$" -- \*.py | grep -v pprint
.PHONY: check_endsemi
check_endsemi:
	$(info doing $@)
	@-git grep -e "\;$$" -- \*.py
.PHONY: check_doublespace
check_doublespace:
	$(info doing $@)
	@-git grep -e "\ \ " -- \*.py
.PHONY: check_endspace
check_endspace:
	$(info doing $@)
	@-git grep -e "\s$$" -- \*.py
.PHONY: check_ops
check_ops:
	$(info doing $@)
	@-git grep -e " = " --or -e " == " --or -e " != " --or -e " < " --or -e " > " --or -e " % " --or -e " / " --or -e " + " --or -e " - " --or -e " <= " --or -e " => " -- \*.py
.PHONY: check_syn
check_syn:
	-git grep ";" -- \*.py
	-git grep " \"," -- \*.py
	-git grep ", " -- \*.py
	-git grep "print\ " -- \*.py
	-git grep --files-without-match "mark@veltzer.net" -- \*.py
.PHONY: clean_compiled
clean_compiled:
	-@rm -f `find . -type f -and \( -name "*.pyo" -or -name "*.pyc" \)`
.PHONY: show_compiled
show_compiled:
	@find . -type f -and -name "*.pyp" -and -name "*.pyc"
.PHONY: show_extra
show_extra:
	@find . -type f -and -not -name "*.py" -and -not -name "Makefile"

include Makefile.prep
