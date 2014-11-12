include /usr/share/templar/make/Makefile

ALL:=$(TEMPLAR_ALL)
ALL_DEP:=$(TEMPLAR_ALL_DEP)

##############
# parameters #
##############
# do you want to show the commands executed ?
# Since we are using ?= for assignment it means that you can just
# set this from the command line and avoid changing the makefile...
DO_MKDBG?=0

########
# code #
########
# silent stuff
ifeq ($(DO_MKDBG),1)
Q:=
# we are not silent in this branch
else # DO_MKDBG
Q:=@
#.SILENT:
endif # DO_MKDBG

#########
# rules #
#########

.DEFAULT_GOAL=all
.PHONY: all
all: $(ALL)
	$(info doing [$@])

.PHONY: clean
clean:
	$(info doing [$@])
	$(Q)git clean -xdf > /dev/null

.PHONY: debug
debug:
	$(info doing [$@])
	$(info ALL is $(ALL))
	$(info ALL_DEP is $(ALL_DEP))

.PHONY: check_all
check_all: check_doublespace check_endspace check_ops check_print check_endsemi check_doublequote
.PHONY: check_doublequote
check_doublequote:
	$(info doing [$@])
	$(Q)make_helper wrapper-noerr git grep \" -- \*.py
.PHONY: check_print
check_print:
	$(info doing [$@])
	$(Q)make_helper wrapper-noerr git grep -e "print " --or -e "print$$" --and --not -e "pprint" -- \*.py
.PHONY: check_endsemi
check_endsemi:
	$(info doing [$@])
	$(Q)make_helper wrapper-noerr git grep -e "\;$$" -- \*.py
.PHONY: check_doublespace
check_doublespace:
	$(info doing [$@])
	$(Q)make_helper wrapper-noerr git grep -e "\ \ " -- \*.py
.PHONY: check_endspace
check_endspace:
	$(info doing [$@])
	$(Q)make_helper wrapper-noerr git grep -e "\s$$" -- \*.py
.PHONY: check_ops
check_ops:
	$(info doing [$@])
	$(Q)make_helper wrapper-noerr git grep -e " = " --or -e " == " --or -e " != " --or -e " < " --or -e " > " --or -e " % " --or -e " / " --or -e " + " --or -e " - " --or -e " <= " --or -e " => " -- \*.py
.PHONY: check_syn
check_syn:
	$(info doing [$@])
	$(Q)make_helper wrapper-noerr git grep ";" -- \*.py
	$(Q)make_helper wrapper-noerr git grep " \"," -- \*.py
	$(Q)make_helper wrapper-noerr git grep ", " -- \*.py
	$(Q)make_helper wrapper-noerr git grep "print\ " -- \*.py
	$(Q)make_helper wrapper-noerr git grep --files-without-match "mark@veltzer.net" -- \*.py

.PHONY: clean_compiled
clean_compiled:
	$(info doing [$@])
	$(Q)-rm -f `find . -type f -and \( -name "*.pyo" -or -name "*.pyc" \)`

.PHONY: show_compiled
show_compiled:
	$(info doing [$@])
	$(Q)find . -type f -and -name "*.pyp" -and -name "*.pyc"

.PHONY: show_extra
show_extra:
	$(info doing [$@])
	$(Q)find . -type f -and -not -name "*.py" -and -not -name "Makefile"
