This task illustrates how exam questions will be posed. This task awards no points and is irrelevant for the bonus system.

Note that the task description consists of:
 - A German description (which is binding in case there are inconsistencies between the German and English versions)
 - An English description
 - A code template, including some commented assertions

Through this exercise, you should become familiar with the logistics of solving exam tasks. In particular, take note of the following:
 - The assertions are commented in the template. The reason for this is that the assertions will all fail for an empty solution. So when you start writing your solution, it makes sense to leave the assertions commented.
 - Once you think that your solution should work correctly, you can uncomment the assertions and run the code again to see if the assertions pass.
 - Note how one assertion checks what happens if the input list is empty: The function should return None. This should be clear implicitely from the task description, but it's not explicitely mentioned. So: always make sure to also consider the assertions to determine how your solution should behave in edge cases.
 - Before you submit the task in the online exam platform, you may comment or delete the assertions, since they are irrelevant for the grading.
 - *Important*: If any assertions included and not commented in the final submissions cause errors, the entire task will be awarded zero points! Remove all assertions before submission if you want to be sure that the task is graded.

_What follows now is the task as it would be posed in the exam platform_

# Deutsch
Implementieren Sie eine Funktion `where_is_waldo`, welche eine Liste von strings `names` als Parameter annimt und den Index des Strings `"Waldo"` innerhalb von `names` zurückgibt. Falls `"Waldo"` mehr als einmal vorkommt, soll der erste Index zurückgegeben werden. Wenn `"Waldo"` nicht in `names` vorkommt, soll die Funktion `None` zurückgegeben.

Beachten Sie die Assertions als Beispiele für die Anwendung von `where_is_waldo`.

# English
Implement a function `where_is_waldo`, which takes a list of strings as a parameter `names` and returns the index of the string `"Waldo"` within `names`. If `"Waldo"` appears more than once, the first index should be returned. If `"Waldo"` is not in `names`, the function should return `None`.

Consider the assertions as examples for how `where_is_waldo` can be used.

```
def where_is_waldo(names):
    pass

# assert(where_is_waldo(["Peter", "Waldo", "John"]) == 1)
# assert(where_is_waldo(["Peter", "Willy", "John"]) == None)
# assert(where_is_waldo([]) == None)
```

Fügen Sie ihre Lösung in folgendes Textfeld ein / Paste your solution into the following text field

_On the exam platform there will be a text field at this location where you can paste and run the code. On ACCESS, you can solve the task as usual by implementing script.py._

