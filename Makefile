include /usr/share/templar/make/Makefile

ALL:=$(TEMPLAR_ALL)
ALL_DEP:=$(TEMPLAR_ALL_DEP)

.PHONY: check
check: check_return check_if check_has_key
	
.PHONY: check_return
check_return:
	@git grep -l -E "return\(.*\)$$" -- '*.py' || exit 0
	@git grep -l -E "return \(.*\)$$" -- '*.py' || exit 0

.PHONY: check_if
check_if:
	@git grep -l -E "if \(" -- '*.py' || exit 0
	@git grep -l -E "if\(" -- '*.py' || exit 0

.PHONY: check_has_key
check_has_key:
	@git grep -l "has_key" -- '*.py' || exit 0
