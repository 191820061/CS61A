from utils import *


def choose(paragraphs, select, k):
    count = -1
    for element in paragraphs:
        if select(element):
            count += 1
        if count == k:
            return element
    return '\'\''


def accuracy(typed, reference):
    typed_words = split(typed)
    reference_words = split(reference)
    if len(typed_words) == 0:
        return 0.0
    correct = int()
    for i in range(len(typed_words)):
        if i == len(reference_words):
            break
        if typed_words[i] == reference_words[i]:
            correct += 1
    return (correct / len(typed_words)) * 100


def wpm(typed, elapsed):
    assert elapsed > 0, 'Elapsed time must be positive'
    return (len(typed) / 5) * (60 / elapsed)


def get_length(word1, word2):
    if len(word1) == 0:
        return len(word2)
    if word1[0] == word2[0]:
        return get_length(word1[1:], word2[1:])
    else:
        return 1 + get_length(word1[1:], word2[1:])


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def fastest_words(game):
    players = range(len(all_times(game)))  # An index for each player
    words = range(len(all_words(game)))  # An index for each word
    result_list = [[] for i in players]
    for i in words:
        min_time = time(game, 0, i)
        min_play = 0
        for player in players:
            play_time = time(game, player, i)
            if play_time < min_time:
                min_time = play_time
                min_play = player
        word = word_at(game, i)
        result_list[min_play].append(word)
    return result_list


def hailstone(n):
    while n != 1:
        if n % 2 == 0:
            yield n
            n = n // 2
        else:
            yield n
            n = n * 3 + 1
    yield n


def repeated(t, k):
    count = 1
    current_number = next(t)
    next_number = next(t)
    while True:
        if current_number == next_number:
            count += 1
            if count == k:
                return next_number
            current_number, next_number = next_number, next(t)
        else:
            count = 1
            current_number, next_number = next_number, next(t)


s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
print(repeated(s, 1))
print(repeated(s, 2))
print(repeated(s, 3))
print(repeated(s, 1))


