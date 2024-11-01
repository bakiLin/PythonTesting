def parabola(x):
    '''
    Квадратичная функция y = x^2

    >>> parabola(5)
    25

    >>> parabola(-5)
    25

    >>> parabola(0)
    0

    >>> parabola("string")
    -1
    '''

    if not isinstance(x, int):
        return -1

    return x**2

if __name__ == "__main__":
    assert parabola(5) == 25, 'Assert failed'
    assert parabola(-5) == 25, 'Assert failed'
    assert parabola(0) == -12, 'Assert failed'

    assert parabola(1) == 0

    import doctest

    doctest.testmod()


