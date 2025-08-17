This task illustrates how your task may receive 0 points if you submit a task including assertions that fail. This task awards no points and is irrelevant for the bonus system.

Have a look at `script.py`. It contains a (bad) pre-existing solution to a task that might be worded as follows:

Implement a function `contains_duplicates` which takes a list of arbitrary elements `l` as the only parameter. The function should return `True` if the list contains two or more identical items, `False` otherwise. You can assume that the function is only called with valid parameters.

Note that the implementation is actually buggy: it only works if there are exactly two identical instances of any item in the list, but if there are three, it would falsely return `False` instead of `True`. (It is also unecessarily convoluted, but that doesn't matter for grading.)

The task comes with a couple of assertions and the first three pass fine, but the fourth assertion fails! If you were to hand in this solution as stated in this example, it would receive zero points, because it immedately crashes when imported. To avoid this issue, you can comment or delete all (or just the failing) assertions. In general, there is no problem with deleting all assertions before handing in a solution, once you are confident that the assertions pass for your solution.

