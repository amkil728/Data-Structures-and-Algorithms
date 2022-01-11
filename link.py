# Linked Lists

class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first, self.rest = first, rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
        

    def __bool__(self):
        return self is not Link.empty

    def __len__(self):
        s, length = self, 0

        while s:
            s, length = s.rest, length + 1

        return length

    def __getitem__(self, i):
        s = self

        while i > 0:
            s, i = s.rest, i - 1
        return s.first

    def __contains__(self, val):
        s = self

        while s:
            if s.first == val:
                return True
            s = s.rest
        return False

    def __iter__(self):
        s = self
        while s:
            yield s.first
            s = s.rest

# Selectors:

def first(s):
    '''Returns the first element of a linked list s.'''
    return s.first

def rest(s):
    '''Returns a linked list containing the rest of the elements of s.'''
    return s.rest

# Predicate

def empty(s):
    """Returns True if the linked list s is empty."""
    return s is Link.empty

# --------------------------------------------------------------------------------------

# Examples

def range_link(start, end):
    """Returns a linked list containing consecutive integers from start upto but not including end.

    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """

    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start + 1, end))

def map_link(f, s):
    """Returns a linked list by applying f to the elements of s.

    >>> map_link(lambda x: x * x, range_link(3, 6))
    Link(9, Link(16, Link(25)))
    """

    if s is Link.empty:
        return s
    else:
        return Link(f(first(s)), map_link(f, rest(s)))

def filter_link(f, s):
    """Returns a linked list with elements e of s for which f(e) is true.

    >>> filter_link(lambda x: x % 2 == 1, range_link(3, 6))
    Link(3, Link(5))
    """

    if s is Link.empty:
        return s
    else:
        x = first(s)
        if f(x):
            return Link(x, filter_link(f, s.rest))
        else:
            return filter_link(f, s.rest) 

# --------------------------------------------------------------------------------------

# Other Functions

def seq_to_link(seq):
    """Returns a linked list containing the elements of a sequence seq."""
    s = Link.empty
    i = len(seq) - 1

    while i >= 0:
        s = Link(seq[i], s)
        i -= 1

    return s

def iter_to_link(it):
    s = Link(next(it), Link.empty)
    temp = s

    while True:
        try:
            temp.rest = Link(next(it), Link.empty)
            temp = temp.rest
        except StopIteration:
            break

    return s

def linked_list(*args):
    """Returns a linked list containing the given arguments as elements."""

    return seq_to_link(args)

def extend_link(s, t):
    """Returns a list with the elements of s followed by those of t."""
    if s is Link.empty:
        return t
    else:
        return Link(first(s), extend_link(rest(s), t))

def reverse_link(s):
    t = Link.empty
    while s:
        s, t = rest(s), link(first(s), t)
    return t

# --------------------------------------------------------------------------------------

four = Link(1, Link(2, Link(3, Link(4))))
seven = Link(5, Link(6, Link(7)))

haste = Link('h', Link('a', Link('s', Link('t', Link('e')))))
words = Link('to', Link('be', Link('or',
                Link('not', Link('to', Link('be'))))))
