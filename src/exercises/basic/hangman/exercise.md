# Hangman

Write a module that implements a "hangman" game.
It starts with a secret word (e.g. "banana"), and the module will have one public function:
Guess(letter) that will either say there is no such letter, or reveal it in the word:

```python
>>>import hangman
??????
>>>guess('a')
?a?a?a
>>> guess('s')
No such letter
?a?a?a
>>> guess('n')
?anana
```

The original game limits the number of mistakes you can make - ignore it for now.

For simplicity, the module should implement just a single game, initialized with a constant
word.  It should use global variables to store state between guess() calls.
Yes, this is bad design - we'll fix all this when we learn classes.

Hint: for simpler design, have a separate function that prints the partially-revealed "?a?a?a"
string based on the current state.

Rewrite your code from the previous exercise as a Hangman class.
It should take the secret word as a constructor argument.
It should store all state on the instance, so that you may play several totally separate games
with several instances.

Subclass the class from the previous exercise and add a counter of the number of mistakes the user made,
telling the user when he has lost.
[Bonus: add various user-friendly checks: tell the user when he is trying a letter he tried
before, don't let him try guessing after he won/lost, etc...]

Write a script that imports the module with the runs a hangman game.
It should receive the secret word as a command-line argument.
It should ask the user for guesses, exiting when he types "exit".
