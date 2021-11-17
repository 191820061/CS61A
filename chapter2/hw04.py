from hw_ADT import make_city, get_name, get_lat, get_lon, tree, label, \
    branches, is_leaf, print_tree, is_tree


def couple(lst1, lst2):
    assert len(lst1) == len(lst2)
    return [[lst1[i], lst2[i]] for i in range(len(lst1))]


from math import sqrt


def distance(city1, city2):
    return sqrt((get_lat(city1) - get_lat(city2)) ** 2 + (get_lon(city1) - get_lon(city2)) ** 2)


def closer_city(lat, lon, city1, city2):
    city = make_city("default", lat, lon)
    if distance(city, city1) <= distance(city, city2):
        return get_name(city1)
    else:
        return get_name(city2)


def nut_finder(t):
    if label(t) == 'nut':
        return True
    for i in branches(t):
        if nut_finder(i):
            return True
    return False


def sprout_leaves(t, values):
    if is_leaf(t):
        return tree(label(t), branches=[tree(v) for v in values])
    return tree(label(t), [sprout_leaves(i, values) for i in branches(t)])


def bigpath(t, n):
    def one(b):
        if b:
            return 1
        else:
            return 0

    if is_leaf(t):
        return one(label(t) >= n)
    else:
        if label(t) >= n:
            return sum([bigpath(b, n - label(t)) for b in branches(t)]) + 1
    array = [bigpath(b, n - label(t)) for b in branches(t)]
    return sum(array)


def bigger_path(t, n):
    way = bigpath(t, n)
    way += sum([bigger_path(b, n) for b in branches(t)])
    return way


t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
print(bigger_path(t, 9))
