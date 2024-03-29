"""
Usage: hangman.py <secret_word>
"""

import sys

from myclass import Hangman  # type: ignore

args = sys.argv[1:]
if len(args) != 1:
    print(__doc__)  # usage message
    sys.exit(2)

print("Type \"exit\" to exit.")
h = Hangman(args[0])
while True:
    line = input("TYPE A LETTER: ")
    if line.strip().lower() in ["exit", "quit"]:
        break
    h.guess(line)
