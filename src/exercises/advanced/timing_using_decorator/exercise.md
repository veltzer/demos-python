# Timing Using Decorator

We want to time how long it takes our functions to run.

Write a decorator called `time_it`, which measures the time it takes a function to run.

Allow the user to get the statistics that you collected at the end of the run.

Here is how I would use the decorator that you wrote:

```python
@time_it
def my_function(...):
    ...
```

make your decorator work on more than one function.

## Hint
* you will need the `time` module to actually know what the time is.
