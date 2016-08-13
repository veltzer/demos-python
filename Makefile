############
# includes #
############
include /usr/share/templar/make/Makefile

##############
# parameters #
##############

########
# code #
########
ALL_PY:=$(shell find src -name "*.py")
ALL_STAMP:=$(addsuffix .stamp, $(basename $(ALL_PY)))

ifeq ($(DO_MKDBG),1)
Q=
# we are not silent in this branch
else # DO_MKDBG
Q=@
#.SILENT:
endif # DO_MKDBG

#########
# rules #
#########
.PHONY: all
all: check_all

.PHONY: check_all
check_all: $(ALL_STAMP)

.PHONY: check
check: check_ws check_return check_if check_has_key

.PHONY: check_ws
check_ws:
	$(info doing [$@])
	$(Q)git grep -E "\s$$" -- '*.py' || exit 0

.PHONY: check_return
check_return:
	$(info doing [$@])
	$(Q)git grep -l -E "return\(.*\)$$" -- '*.py' || exit 0
	$(Q)git grep -l -E "return \(.*\)$$" -- '*.py' || exit 0

.PHONY: check_if
check_if:
	$(info doing [$@])
	$(Q)git grep -l -E "if \(" -- '*.py' || exit 0
	$(Q)git grep -l -E "if\(" -- '*.py' || exit 0

.PHONY: check_has_key
check_has_key:
	$(info doing [$@])
	$(Q)git grep -l "has_key" -- '*.py' || exit 0

$(ALL_STAMP): %.stamp: %.py
	$(info doing [$@])
	$(Q)scripts/syntax_check.py $<
	$(Q)touch $@

.PHONY: debug_me
debug_me:
	$(Q)$(info ALL_STMAP is $(ALL_STAMP))

.PHONY: show_shbang
show_shbang:
	$(Q)find src -name "*.py" -and -executable -exec head -1 {} \; | sort | uniq
