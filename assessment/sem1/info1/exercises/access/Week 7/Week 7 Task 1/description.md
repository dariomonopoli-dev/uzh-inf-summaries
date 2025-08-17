This task illustrates how assertions work. This task awards no points and is irrelevant for the bonus system.

Python's `assert` function has a very simple behavior:

If the expression passed to `assert` evaluates as `True`, nothing noteworthy happens. The code simply continues. We say that such an assertion "passes". Here are some examples for assertions that would pass:

```
assert(True)
assert(1 == 1)
assert(int("1") == 1)
assert("1".isdigit())
assert(not "a".isdigit())
assert(abs(-5) == 5)
```

If the expression passed to `assert` evaluates as `False`, an "AssertionError" is raised and the program crashes. We say that such an assertion "fails". Here are some examples for failing assertions:

```
assert(False)
assert(None)
assert(int("1") == "1")
assert("a".isdigit())
assert(not "1".isdigit())
assert(abs(-5) == -5)
```

To help you figure out if your solution is any good, we provide a few assertions checking some of the expected functionality in the exam. These assertions call the solution function with certain inputs and compare the resulting return value to an expected value.

Have a look at `script.py`. It contains a pre-existing solution to a task that might be worded as follows:

Implement a function `invert_casing` which takes a string `text` as the only parameter. The function should return the string with the casing inverted for all characters in the string. You can assume that the function is only called with valid parameters.

As you can see, the function implementation is followed by three assertions. All these assertions pass because the implementation does indeed return the expected values.

Try changing the assertions. See if you can write other assertions which pass, but also write some that fail. Also note that if you remove the implementation of `invert_casing`, i.e.:

```
def invert_casing(text):
    pass
```

then all the assertions fail.

