def coin_change(n, coins):
    if n == 0:
        return True
    elif n < 0 or not coins:
        return False
    coin = coins.pop()
    return coin_change(n, list(coins)) or coin_change(n - coin, list(coins))


def amount(coins):
    if not coins:
        return [0]
    coin = coins[0]
    rest = amount(list(coins[1:]))
    return sorted(rest + [k + coin for k in rest if k + coin not in rest])


print(amount([2, 7, 1, 8, 2]))
