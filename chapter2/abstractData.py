def mobile(left, right):
    """Construct a mobile from a left arm and a right arm."""
    assert is_arm(left), "left must be a arm"
    assert is_arm(right), "right must be a arm"
    return ['mobile', left, right]


def is_mobile(m):
    """Return whether m is a mobile."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'


def left(m):
    """Select the left arm of a mobile."""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]


def right(m):
    """Select the right arm of a mobile."""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]


def arm(length, mobile_or_planet):
    """Construct a arm: a length of rod with a mobile or planet at the end."""
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ['arm', length, mobile_or_planet]


def is_arm(s):
    """Return whether s is a arm."""
    return type(s) == list and len(s) == 3 and s[0] == 'arm'


def length(s):
    """Select the length of a arm."""
    assert is_arm(s), "must call length on a arm"
    return s[1]


def end(s):
    """Select the mobile or planet hanging at the end of a arm."""
    assert is_arm(s), "must call end on a arm"
    return s[2]


def planet(size):
    assert size > 0
    return ['planet', size]


def size(w):
    assert is_planet(w), 'must call size on a planet'
    return w[1]


def is_planet(w):
    """Whether w is a planet."""
    return type(w) == list and len(w) == 2 and w[0] == 'planet'


def examples():
    t = mobile(arm(1, planet(2)),
               arm(2, planet(1)))
    u = mobile(arm(5, planet(1)),
               arm(1, mobile(arm(2, planet(3)),
                             arm(3, planet(2)))))
    v = mobile(arm(4, t), arm(2, u))
    return t, u, v


def total_weight(m):
    if is_planet(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a planet"
        return total_weight(end(left(m))) + total_weight(end(right(m)))


def balanced(m):
    assert is_mobile(m)
    if is_mobile(end(left(m))) and balanced(end(left(m))) == False:
        return False
    if is_mobile(end(right(m))) and balanced(end(right(m))) == False:
        return False
    return (total_weight(end(left(m))) * length(left(m))) == (total_weight(end(right(m))) * length(right(m)))


from ADT import tree, label, branches, is_leaf, print_tree


def totals_tree(m):
    assert is_mobile(m) or is_planet(m)
    if is_mobile(m):
        return tree(total_weight(m), [totals_tree(end(left(m))), totals_tree(end(right(m)))])
    elif is_planet(m):
        return tree(size(m))


def preorder(t):
    result = list()
    node_stack = list([t])
    while len(node_stack) != 0:
        cur = node_stack.pop()
        result.append(label(cur))
        if len(cur) > 1:
            for i in branches(cur)[::-1]:
                node_stack.append(i)
    return result


def insert_items(lst, entry, elem):
    n = len(lst)
    i = 0
    while i < n:
        if lst[i] == entry:
            lst.insert(i + 1, elem)
            i += 1
            n += 1
        i += 1
    return lst


def has_path(t, word):
    assert len(word) > 0, 'no path for empty word.'
    if label(t) != word[0]:
        return False
    elif len(word) == 1:
        return True
    for b in branches(t):
        if has_path(b, word[1:]):
            return True
    return False


greetings = tree('h', [tree('i'), tree('e', [tree('l', [tree('l', [tree('o')])]), tree('y')])])
print(has_path(greetings, 'hell'))
