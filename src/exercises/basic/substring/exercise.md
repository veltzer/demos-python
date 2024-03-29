# Substring

Write a function called `substring(s1, s2)` which
receives two strings and returns True iff (if and only if)
s1 is a substring of s2, otherwise return `False`.

Examples:

```python
hi, Ship -> True
shi, Ship -> False (notice the different case for the letter 's')
Ships, Ship -> False (s2 is a substring of s1 but s1 is NOT a substring of s2)
```

## hints
* You can iterate the characters of string with a for loop.
For example:

```python
my_string = "hello"
for c in my_string:
    print(c)
```

will print all the characters in the string "hello", one on each line.

* if you have a string named 's' and you want to access it's nth character then s[n] will give you that character (n should be an integer and represent a valid position within the string)

* if you want to access a substring of a string from location x to location y (not including y) then `s[x:y]` will give you that slice of the string.
