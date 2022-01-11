# Trees

# Abstract data type tree:
# a tree has a root label, and a list of branches (which may be empty)
# each branch is also a tree

# Other definitions:
# a leaf is a tree with no branches
# the root of the tree is the label at which it starts

# Constructor

class BTree:
	def __init__(self, left, right):
		self.left, self.right = left, right

def tree(label, branches=[]):
    '''Returns a tree with given label and branches.'''

    # make sure that all branches are trees
    for branch in branches:
        assert is_tree(branch), 'branches must also be trees'

    # if branches is not a list, convert it so we can add it to a list
    return [label] + list(branches)

# Predicate

def is_tree(obj):
    '''Checks if the given object is a tree.'''

    # If the object is not a list or has no items, it is not a tree
    if type(obj) != list or obj == []:
        return False

    # if any of the branches of the object is not a tree, it is also not a tree
    for branch in branches(obj):
        if not is_tree(branch):
            return False

    # otherwise, the object is a tree
    return True

# Selectors

def label(t):
    '''Returns the label of a tree.'''
    return t[0]

def branches(t):
    '''Returns the list of branches of a tree.'''
    return t[1:]

# --------------------------------------------------------------------------------------------------

# Basic Functions

def is_leaf(t):
    '''Checks if the given tree is a leaf.'''

    # a leaf has no branches, so its list of branches should be empty
    return not branches(t)

def count_leaves(t):
    '''Counts the leaves of a tree.'''
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])

def leaves(t):
    '''Returns a list containing the leaf labels of a tree.'''
    if is_leaf(t):
        return [label(t)]
    else:
        return sum([leaves(b) for b in branches(t)], [])

def print_tree(t, indent=0):
    '''Prints a tree.'''
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

# --------------------------------------------------------------------------------------------------

# Container Functions

def map_tree(f, t):
    '''Returns a tree by applying f to the labels of t.'''
    head = f(label(t))
    bs = [map_tree(f, b) for b in branches(t)]
    return tree(head, bs)

# --------------------------------------------------------------------------------------------------

# Example Functions

def increment_leaves(t):
    '''Returns a tree with the same labels as t, except leaf labels are incremented by 1.'''

    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)

def increment(t):
    '''Returns a tree with ALL labels of t incremented by 1.'''
    return tree(label(t) + 1, [increment(b) for b in branches(t)])

# --------------------------------------------------------------------------------------------------

# Examples

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left) + label(right), [left, right])

numbers = tree(1, [tree(2, [tree(3, [tree(4)]), tree(4, [tree(1), tree(5), tree(6)]), tree(1)]),
                   tree(7, [tree(8), tree(9)])])

haste = tree('h', [tree('a', [tree('s'), tree('t')]),
                 tree('e')])
