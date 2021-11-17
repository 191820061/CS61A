def ration_function(n, d):
    def select(name):
        if name == 'n':
            return n
        else:
            return d

    return select


def review_list():
    digit = [1, 8, 2, 8]
    print(len(digit))  # list length
    print(digit[3])  # list index
    new_digit = [2, 7] + digit * 2
    print(new_digit)


def review_for_in_statement():
    for i in list([4, 56, 47]):
        print(i)
    for i in range(4, 15):
        print(i)

    for x, y in [[1, 4], [2, 5], [3, 3], [4, 6]]:
        if x == y:
            print("fuck you {0}{1}".format(x, y))


def review_range():
    print(list(range(-2, 2)))
    print(list(range(4)))  # the default start value is 0
    for i in range(1, 4):  # range is iterable
        print(i)


def review_slicing():
    digit = [1, 2, 4, 8]
    print(digit[0:2])
    print(digit[0:])
    print(digit[0:4])


def review_is():
    a = [4, 5, 6, 7]
    b = [4, 5, 6, 7]
    print(a is b)
    print(a == b)


def review_iter():
    a = [4, 7, 8, 9]
    a_iter = iter(a)
    print(next(a_iter))
    print(next(a_iter))
    print(next(a_iter))
    print(next(a_iter))
    d = {"one": 1, "two": 2, "three": 3, "four": 4}
    d_iter = iter(d)
    print(next(d_iter))
    print(next(d_iter))
    print(next(d_iter))
    print(next(d_iter))
    print(d_iter)


def plus_minus(x):
    yield x
    yield -x


def a_then_b(a, b):
    yield from a
    yield from b


def review_filter():
    a = [4, 5, 6, 7, 8]

    def odd(value):
        return value % 2 == 1

    def even(value):
        return value % 2 == 0

    yield from list(filter(odd, a))
    yield from list(filter(even, a))


def review_map():
    def add(n):
        return n + 1

    print(list(map(add, review_filter())))


def review_all_any():
    a = [1, 4, 5, 8, 9, 7, 8]
    b = [0, 1, 4, 5, 8, 9, 7, 8]
    c = [0, 0, 0, 0]
    d = []
    print(all(a))
    print(all(b))
    print(all(d))
    print(any(a))
    print(any(b))
    print(any(c))
    print(any(d))


def review_box_pointer():
    digit = [4, 5, 6]
    new_digit = [0, digit]
    print(new_digit)


from operator import add, mul, sub


def order_order(ops):
    def apply(x, y):
        print(ops[0](x, y))
        return order_order(ops[1:] + [ops[0]])

    return apply


def review_dict():
    digit = [-10, 1, 4, 5, 7]
    print(max(digit, key=lambda x: -x))


review_all_any()
