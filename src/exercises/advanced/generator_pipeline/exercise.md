# Generator Pipeline

Build a text processing program which is based on building a pipeline of generators.
The user of your program will ultimately determine in which order the generators are to
be applied.

The "source" generator, the one that gives you the data to work on, will simply retrieve
all the lines in the attached soliloquy.

Here are other generators to be implemented:
* splitter - gets a strings from another generator and splits the strings according to space
* punctuation remover - removes things like commas, period etc..
* lower-caser - lower cases everything that it gets
* suffix remover - removes common suffixes from strings it gets (e.g. "ing", "ed")

Allow the user to determine in which order to apply the generators.

Print out the output from the last generator.

hint:
Start simple, don't allow the user to determine the order of generators at first.
See that all generators work.
And only then add the flexibility of allowing the user to determine the order of generators.
