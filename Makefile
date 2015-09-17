include /usr/share/templar/make/Makefile

ALL:=$(TEMPLAR_ALL)
ALL_DEP:=$(TEMPLAR_ALL_DEP)

ALL_PY:=$(shell find examples exercises -name "*.py")
ALL_STAMP:=$(addsuffix .stamp, $(basename $(ALL_PY)))

.PHONY: check_all
check_all: $(ALL_STAMP)

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

$(ALL_STAMP): %.stamp: %.py
	$(info doing [$@])
	@scripts/syntax_check.py $<
	@touch $@

.PHONY: debug_me
debug_me:
	echo $(ALL_STAMP)

.PHONY: show_shbang
show_shbang:
	find . -name "*.py" -and -executable -exec head -1 {} \; | sort | uniq
