#  Name:
#  Email:

# Q1.

class Mobile:
    """A simple binary mobile that has branches of weights or other mobiles.

    >>> Mobile(1, 2)
    Traceback (most recent call last):
        ...
    TypeError: 1 is not a Branch
    >>> m = Mobile(Branch(1, Weight(2)), Branch(2, Weight(1)))
    >>> m.weight
    3
    >>> m.is_balanced()
    True
    >>> m.left.contents = Mobile(Branch(1, Weight(1)), Branch(2, Weight(1)))
    >>> m.weight
    3
    >>> m.left.contents.is_balanced()
    False
    >>> m.is_balanced() # All submobiles must be balanced for m to be balanced
    False
    >>> m.left.contents.right.contents.weight = 0.5
    >>> m.left.contents.is_balanced()
    True
    >>> m.is_balanced()
    False
    >>> m.right.length = 1.5
    >>> m.is_balanced()
    True
    """

    def __init__(self, left, right):
        "*** YOUR CODE HERE ***"
        msg = "{} is not a Branch"
        self.left = left
        self.right = right
        if type(self.left) != Branch:
            raise TypeError(msg.format(self.left))
        if type(self.right) != Branch:
            raise TypeError(msg.format(self.right))
    @property
    def weight(self):
        """The total weight of the mobile."""
        "*** YOUR CODE HERE ***"
        return self.left.contents.weight + self.right.contents.weight

    def is_balanced(self):
        """True if and only if the mobile is balanced."""
        "*** YOUR CODE HERE ***"


        return True if self.left.torque \
               == self.right.torque and self.left.contents.is_balanced() \
               and self.right.contents.is_balanced() else False
        

def check_positive(x):
    """Check that x is a positive number, and raise an exception otherwise.

    >>> check_positive('hello')
    Traceback (most recent call last):
    ...
    TypeError: hello is not a number
    >>> check_positive('1')
    Traceback (most recent call last):
    ...
    TypeError: 1 is not a number
    >>> check_positive(-2)
    Traceback (most recent call last):
    ...
    ValueError: -2 <= 0
    """
    "*** YOUR CODE HERE ***"
    if type(x) != int:
        raise TypeError("{} is not a number".format(x))
    else:
        if x <= 0:
            raise ValueError("{} <= 0".format(x))


class Branch:
    """A branch of a simple binary mobile."""

    def __init__(self, length, contents):
        if type(contents) not in (Weight, Mobile):
            raise TypeError(str(contents) + ' is not a Weight or Mobile')
        check_positive(length)
        self.length = length
        self.contents = contents

    @property
    def torque(self):
        """The torque on the branch"""
        return self.length * self.contents.weight


class Weight:
    """A weight."""
    def __init__(self, weight):
        check_positive(weight)
        self.weight = weight

    def is_balanced(self):
        return True

# Q2.

def interpret_mobile(s):
    """Return a Mobile described by string s by substituting one of the classes
    Branch, Weight, or Mobile for each occurrenct of the letter T.

    >>> simple = 'Mobile(T(2,T(1)), T(1,T(2)))'
    >>> interpret_mobile(simple).weight
    3
    >>> interpret_mobile(simple).is_balanced()
    True
    >>> s = 'T(T(4,T(T(4,T(1)),T(1,T(4)))),T(2,T(10)))'
    >>> m = interpret_mobile(s)
    >>> m.weight
    15
    >>> m.is_balanced()
    True
    """
    next_T = s.find('T')        # The index of the first 'T' in s.
    if next_T == -1:            # The string 'T' was not found in s
        try:
            return eval(s)      # Interpret s
        except TypeError as e:
            return None         # Return None if s is not a valid mobile
    for t in ('Branch', 'Weight', 'Mobile'):
        "*** YOUR CODE HERE ***"
    return None


# Q3.

class Stream:
    """A lazily computed recursive list."""

    class empty:
        def __repr__(self):
            return 'Stream.empty'
    empty = empty()

    def __init__(self, first, compute_rest=lambda: Stream.empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest

    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest

    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))

    def __iter__(self):
        """Return an iterator over the elements in the stream.

        >>> list(zip(range(6), ints))
        [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
        """
        "*** YOUR CODE HERE ***"

    def __getitem__(self, k):
        """Return the k-th element of the stream.

        >>> ints[5]
        6
        >>> increment_stream(ints)[7]
        9
        """
        "*** YOUR CODE HERE ***"

def increment_stream(s):
    """Increment all elements of a stream."""
    return Stream(s.first+1, lambda: increment_stream(s.rest))

# The stream of consecutive integers starting at 1.
ints = Stream(1, lambda: increment_stream(ints))


# Q4.

def scale_stream(s, k):
    """Return a stream over the elements of s scaled by a number k.

    >>> s = scale_stream(ints, 5)
    >>> s.first
    5
    >>> s.rest
    Stream(10, <...>)
    >>> scale_stream(s.rest, 10)[2]
    200
    """
    "*** YOUR CODE HERE ***"


# Q5.

def merge(s0, s1):
    """Return a stream over the elements of increasing s0 and s1, removing
    repeats.

    >>> twos = scale_stream(ints, 2)
    >>> threes = scale_stream(ints, 3)
    >>> m = merge(twos, threes)
    >>> [m[i] for i in range(10)]
    [2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    if s0 is Stream.empty:
        return s1
    elif s1 is Stream.empty:
        return s0

    e0, e1 = s0.first, s1.first
    "*** YOUR CODE HERE ***"

def make_s():
    """Return a stream over all positive integers with only factors 2, 3, & 5.

    >>> s = make_s()
    >>> [s[i] for i in range(20)]
    [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36]
    """
    def rest():
        "*** YOUR CODE HERE ***"
    s = Stream(1, rest)
    return s

