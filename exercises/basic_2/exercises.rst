.. -*- rst -*-
.. You can create an HTML file from this file using docutils
.. which is nicer to read.
.. (it was generated from this using http://docutils.sf.net)

===========================================
 Python Exercises: Types, Loops, Functions
===========================================

Hi.  Here are some exercise that you should be able to do at the current 
point in the course.  If you have any questions, please don't hesitate 
to contact me at <beni.cherniavsky@gmail.com>.  I'll try to answer same day.

I tried to build them in steps, so you can at least solve them
partially, if you don't know how to solve the full problem.

All exercises come with solutions.  It's OK if you fail to solve a few
and peek at the solutions; and it's a good idea to look at my
solutions even if your solution works perfectly.  But if there is
anything unclear in my solutions, please mail me.

If you don't remember something from the course, the `Python
Tutorial`_ will probably serve you better than the course slides.
(It's also accessible among the Python docs that open when you press
F1 in IDLE.)  Specifically, what you learnt is in chapters 3-5 of the
tutorial (except 4.7 and 5.1.3-5, the course covers these topics
later).

Also, don't forget the builtin ``help()`` function.  And again, mail
me if you get stuck.

.. _Python Tutorial: http://docs.python.org/tutorial/


Warmup
======

The following code right-aligns several lines of text::

    def right_align_to(lines, width):
	"""Right-align all lines to given width."""
	result = []
	for line in lines:
	    result.append(line.rjust(width))
	return result

    for line in right_align_to(['foo', 'x', '12345678'], 8):
	print line

which prints::

         foo
	   x
    12345678

Things to note in this example:

- ``def`` defines a function.  You barely reached the functions
  chapter in the course - but as you see it's very simple.  In most of
  these exercise, you won't *have* to split your code into functions,
  but it's frequently a good idea.

- See how I initialized ``result`` to an empty list and then did a
  loop that appends elements to it?  Remember it, it's a very common
  way to build a list.  [In chapter 4, `Data Processing`, you'll learn
  a shorthand syntax for it.  But you don't need it for now.]

Up and running
--------------

First, try to run this example and see that it works.  This is just to
check that you remember how to use IDLE.

- If you're working from IDLE's `Python Shell` window, remember that
  you have to press Enter twice at the end of a complex command, like
  ``def`` or ``for``.  [Copy-pasting both commands at once won't work,
  IDLE's shell window doesn't support it.]

- If you're working from IDLE's editing window (File→New, Save As with
  ``.py`` extension), just press F5.

Exercise 1: Width
-----------------

Modify this code so that instead of being told the width (8 in this
case), it will automatically compute the length of the longest line.

**Hints**:

- ``len("abc")`` returns 3.

- ``max([3,1,8])`` returns 8.

Solution: ``width.py``


2. Table
========

You are given a list of 3 columns, each being a list of strings (all
of the same length)::

    columns = [['H', 'He', 'Li', 'Be'],
	       ['Hidrogen', 'Helium', 'Litium', 'Berilium'],
	       ['1.008', '4.003', '6.941', '9.012']]

Your task is to print it as a nice ASCII table.

Exercise 2A: fixed layout
-------------------------

For starters, assume there are exactly 3 columns and print each column
10 characters wide::

    +----------+----------+----------+
    |H         |Hidrogen  |1.008     |
    +----------+----------+----------+
    |He        |Helium    |4.003     |
    +----------+----------+----------+
    |Li        |Litium    |6.941     |
    +----------+----------+----------+
    |Be        |Berilium  |9.012     |
    +----------+----------+----------+

This is quite easy.  The only tricky part is that the data is arranged
by columns, so you need to access the i'th element of each column in
parallel.

**Hints**:
    - ``"-" * 10`` returns ``"----------"``.
    - ``"Helium".ljust(10)`` returns ``"Helium "``.
    - Try ``zip(columns[0], columns[1], columns[2])`` in the
      interpreter.  If you don't understand how this helps you, peek
      at the solution - it's an useful function to know!

Solution: ``table_fixed.py``
    
Exercise 2B: Auto-fit
---------------------

Now, improve it by computing the proper width for each column::

    +--+--------+-----+
    |H |Hidrogen|1.008|
    +--+--------+-----+
    |He|Helium  |4.003|
    +--+--------+-----+
    |Li|Litium  |6.941|
    +--+--------+-----+
    |Be|Berilium|9.012|
    +--+--------+-----+

This obviously requires doing 2 passes over the data - one to compute
the width for each column, one to print the table.

Solution: ``table_autofit.py``


3. Map
======

You're given a dictionary representing a (very simplified) map of
Frodo's travels around Middle Earth::

    places = {
	'Shire': {'leave': 'Bree', 'stay': 'DEATH'},
	'DEATH': {},
	'Bree': {'with Strider': 'Rivendell', 'alone': 'DEATH'},
	'Rivendell': {'over mountains': 'DEATH', 'through Moria': 'Lorien'},
	'Lorien': {'down Anduin': 'Falls of Rauros'},
	'Falls of Rauros': {'down Anduin': 'Minas Tirith',
			    'east': 'Ithilien'},
	'Ithilien': {'south': 'Black Gate'},
	'Black Gate': {'in': 'DEATH', 'follow Gollum': 'Minas Morgul'},
	'Minas Morgul': {'road': 'DEATH', 'tunnel': 'Mordor'},
	'Mordor': {'eagles': 'Minas Tirith'},
	'Minas Tirith': {'return home': 'Shire (tired)'},
	'Shire (tired)': {'stay': 'Shire (tired)', 'retire': 'the West'},
	'the West': {}
	}

For each place there is a sub-dictionary mapping actions Frodo could
take and where they would lead him.  (Many lead to 'DEATH', from which
there are no more actions possible ;-).

Exercise 3A: Walk
-----------------

Such a dictionary is all you need for a (very simple) text-based
role-playing game!  Each time it should print the current place and
the list of actions, and ask the user which action to take.

Bonuses: present a nice interface, don't crush on illegal input, allow
exiting the game.

**Hints**:

- ``raw_input()`` reads a line from the user and returns it.

Solution: ``map_walk.py``

Exercise 3B: Search
-------------------

You're now in Rivendell, and you've just volunteered to take the ring
to Mordor, though you do not know the way.  Can you write a program
that tries to find a way?

For simplicity, we're only looking for sequences of at most 7 actions.

If it simplifies matters for you, you don't have to find the sequence
of actions, just check *whether* it's possible (in no more than 7
steps).

**Hints**: 

- If you have no idea how to solve this, here is a simple approach
  that works.  You'll maintain a dictionary of places to which you
  know the way (the keys will be the action sequences to reach them).

  - Initialize it with only 'Rivendell' (the way to which is [] - no
    actions required).

  - Repeat 7 times: for any place P to which you know the way, for any
    action A leading from P to Q to which you don't yet know the way,
    set ``way_to[Q] = way_to[P] + [A]``.

- If you get a "dictionary changed size during iteration" error, it
  means you should do ``for k in dictionary.keys():`` instead of ``for
  k in dictionary:``.

Still lost?  Read the solution, it's shorter that you'd expect.

Solution: ``map_search.py``


4. RPN Calculator
=================

A "Reverse Polish Notation" calculator takes input in a strange form,
where operators come after the operands::

    2 2 + 5 *

which means (2 + 2) * 5.  There is an extremely simple way to compute
RPN expressions, using a stack:

- When you see a number, push it onto the stack.

- When you see an operator, pop 2 operands from the stack, and push
  the result on the stack.

Write a program that does this, printing the stack after each word::

    []
    2
    [2.0]
    2
    [2.0, 2.0]
    +
    [4.0]
    5
    [4.0, 5.0]
    *
    [20.0]

**Hints**:

- A list works great to represent a stack - use ``.append(value)`` and
  ``.pop()`` methods.

Solution: ``rpn_calculator.py`` (Read this solution!  It will teach
you something about using functions in unexpected ways.)


5. Make clone
=============

Make is a tool that reads a file describing files that can be produced
from other files (e.g. executable from sources), and what commands
have to be run to do it (e.g. compiler).  It compares file
modification dates, and only regenerates the files whose dependecies
changed.

In this exercise, you'll write a very simplified version of Make.
You'll only handle dependecy lists (without commands) and you'll
ignore file modification times (always assuming everything need to be
rebuilt).

Exercise 5A: parsing
--------------------

Write a function that can parse a file like ``make.txt``::

    all:app
    app:a.o b.o
    a.o:a.c
    b.o:b.c

and return a dictionary giving for each target a list of files on
which it depends::

    {'all': ['app'], 
     'a.o': ['a.c'], 
     'b.o': ['b.c'], 
     'app': ['a.o', 'b.o']}

**Hints**:

- The simplest way to read a file line-by-line is ``for line in
  open("make.txt"):``.

- ``"foo:bar".split(":")`` returns ['foo', 'bar'].

**Bonus**: also handle command lines (see ``make_bonus.txt``).

Exercise 5B: solving
--------------------

Now write a function that takes such a dictionary and returns a list
of files that have to be generated.  To build 'all', the result would be::

    ['a.o', 'b.o', 'app', 'all']

Why?  To build 'all' we must first build 'app', but to build 'app', we
must first build 'a.o' and 'b.o'.  (They in turn depend on 'a.c' and
'b.c' but since are no rules for how to build them, Make assumes they
are existing source files.)

For simplicity, assume that different files won't have common
dependencies (Make handles that smartly, building each file at most
once; you don't have to).

**Hints**:

- This is a classical use case for recursion.  There are 2 cases:

  - Source files (no rule to build): ``plan('a.c') == []``
  - Generated files: ``plan('app') == plan('a.o') + plan('b.o') + ['app']``

**Bonus**: if you also parsed the commands, after computing the plan,
show which commands would be executed.

Solutions: ``make.py``, ``make_bonus.py``


6. Lasers
=========

[Credit: this exercise is shamelessly stolen from
http://stackoverflow.com/questions/1480023/code-golf-lasers]

You are given a file such as ``lasers_hit.txt``::

    #########
    #>   \  #
    #  /  x #
    #  \ /  #
    #########

or ``lasers_miss.txt``::

    #########
    #> \ \  #
    #     x #
    #  \ /  #
    #########

which describes a rectangular room.

- The square with ``>`` (could also be ``<`` / ``v`` / ``^``) emits a
  laser beam.

- The laser beam travels empty spaces, and is reflected at 90° by
  ``/`` and ``\`` mirrors.

- The ``x`` is the target, ``#`` are walls.

Your goal is to determine whether the beam ends up hitting the target, 
or anything else (wall, or in rare cases the emitter).  Cute, ha?

For starters, assume the beam emitter is at (1, 1) and points to the
right.  When the rest works, look for the emitter.

**Hints**:

- ``open(fname).readlines()`` returns a list of lines.

- At any point, your state can be described by (x, y, direction).

- The next (x, y) is determined by current (x, y) plus the direction.

- The next direction is determined by room[y][x] and current direction.

- Try to use dictionaries instead of long repetitive if..elif
  statements.  Think about what you learned in the Map and RPN
  calculator exercises...

- Add debugging prints to display your position after every iteration.

Solution: ``lasers.py``
