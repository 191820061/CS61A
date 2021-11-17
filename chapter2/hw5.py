from ADT import tree, label, branches, is_leaf, print_tree


def make_withdraw(balance, password):
    locked_list = list()

    def withdraw(money, pwd):
        nonlocal balance
        if len(locked_list) >= 3:
            return "Your account is locked. Attempts: " + str(locked_list)
        if pwd == password:
            if money > balance:
                return 'Insufficient funds'
            else:
                balance -= money
                return balance
        else:
            locked_list.append(pwd)
            return 'Incorrect password'

    return withdraw


def make_joint(withdraw, old_pass, new_pass):
    def get_another(money, pwd):
        if pwd == old_pass or pwd == new_pass:
            return withdraw(money, old_pass)
        return withdraw(money, pwd)

    result = withdraw(0, old_pass)
    if type(result) != str:
        return get_another
    else:
        return result


def permutations(seq):
    if not seq:
        yield []
    else:
        for perm in permutations(seq[1:]):
            for i in range(len(seq)):
                yield perm[:i] + [seq[0]] + perm[i:]


def lookups(k, key):
    if label(k) == key:
        yield lambda v: label(v)
    for i in range(len(branches(k))):
        for j in lookups(branches(k)[i], key):
            yield helper(i, j)


def helper(i, f):
    def test(v):
        return f(branches(v)[i])
    return test


k = tree(5, [tree(7, [tree(2)]), tree(8, [tree(3), tree(4)]), tree(5, [tree(4), tree(2)])])
v = tree('Go', [tree('C', [tree('C')]), tree('A', [tree('S'), tree(6)]), tree('L', [tree(1), tree('A')])])
print([f(v) for f in lookups(k, 2)])
