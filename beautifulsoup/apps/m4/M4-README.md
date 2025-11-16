# Milestone-4

## Objective

To make the main `BeautifulSoup` object iterable, allowing a user to loop through all nodes in the parse tree using a standard `for node in soup:` loop.

## Implementation

To make the `BeautifulSoup` class iterable, I added Python's magic method `__iter__` to the `BeautifulSoup` class definition within the `bs4/__init__.py` file.

### Core Code

```python
# Added to class BeautifulSoup(Tag) in bs4/__init__.py:

def __iter__(self):
    """
    Make the BeautifulSoup object iterable (for Milestone 4).

    This allows for a simple loop like:
    for node in soup:
        print(node)

    It iterates over all nodes in the parse tree (descendants)
    in document order.
    """
    # self.descendants is already a generator that perfectly
    # meets the requirement: it lazy-loads all nodes
    # one at a time and does not create a list.
    return iter(self.descendants)
```


## Design Rationale

There was a critical constraint in the assignment: "**you should not collect the nodes of the tree onto a list in order to iterate over them.**"

This constraint rules out any simple (but inefficient) solution that first builds a list and then returns the list's iterator. It requires a *lazy-loading* solution that "produces one node at a time" during iteration.

The best way to achieve this in Python is with a **generator**.

1.  The `BeautifulSoup` class inherits from the `Tag` class.
2.  The `Tag` class already provides a **property** named `self.descendants`.
3.  `self.descendants` **is already a generator**. It lazily `yield`s all descendant nodes (tags, strings, etc.) in document order (depth-first, pre-order traversal).
4.  This existing generator perfectly fulfills all the assignment's requirements:
        * It does not collect nodes into a list, making it highly memory-efficient (O(1) memory).
        * It "produces one node at a time."
        * It traverses "all nodes."

Therefore, my implementation of the `__iter__` method is very concise: it simply returns the iterator for the `self.descendants` generator (`iter(self.descendants)`). This delegates the iteration request directly to the efficient traversal logic already built into BeautifulSoup.