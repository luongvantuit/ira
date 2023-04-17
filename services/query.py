import html
from nltk.tokenize import word_tokenize
from os import walk, getcwd
from os.path import join

# Assignment 01
# - 1 Read all file in directories


def get_all_path_files(path_dir):
    _files = []
    _ids = []

    for root, directories, files in walk(path_dir):
        _files.extend([join(path_dir, f) for f in files])
        _ids += files

    return _files, _ids


def get_token_from_file(path_file: str):
    f = open(path_file, 'r', encoding='ISO-8859-1')
    content = html.unescape(f.read())
    f.close()

    tokens = word_tokenize(content)
    return tokens

# - 2 Tokenize all document


def get_tokenize_all_doc():
    tokens = []
    path = join(getcwd(), 'dat/reuters/test')
    path_files, _ids= get_all_path_files(path_dir=path)
    for f in path_files:
        tokenize = get_token_from_file(f)
        tokens.append([t.lower() for t in tokenize])
        # tokens.append(get_token_from_file(f))
    return tokens, _ids


def get_dictionary():
    all_tokens, _id = get_tokenize_all_doc()
    _size = len(all_tokens)

    vocabulary = []
    for tokens in all_tokens:
        vocabulary += tokens
    vocabulary = list(dict.fromkeys(vocabulary))

    dictionary = dict()
    for i in vocabulary:
        coll = []
        for j in range(0, _size):
            if i in all_tokens[j]:
                coll.append(_id[j])
        dictionary[i] = coll

    return dictionary

# Assignment 02
# And (&&) two list


def _and(_d1, _d2):
    _all = sorted(list(dict.fromkeys(_d1 + _d2)))
    result = []
    for i in _all:
        if i in _d1 and i in _d2:
            result.append(i)
    return result

# Or (||) two list


def _or(_d1, _d2):
    return list(dict.fromkeys(_d1 + _d2))

# Search by key for dictionary vocabulary


def search(dictionary, _01):
    return sorted(dictionary[_01.lower()])

# Search by two key with operator And (&&)


def search_and(dictionary, _01, _02):
    _d1 = search(dictionary, _01)
    _d2 = search(dictionary, _02)
    return sorted(_and(_d1, _d2))

# Search by two key with operator Or (||)


def search_or(dictionary, _01, _02):
    _d1 = search(dictionary, _01)
    _d2 = search(dictionary, _02)
    return sorted(_or(_d1, _d2))


def search_not_of(dictionary, _01):
    _ids = []
    for k in dictionary:
        _ids.extend(search(dictionary, k))
    # Filter
    _ids = list(dict.fromkeys(_ids))
    result = []
    for _id in _ids:
        if _id not in search(dictionary, _01):
            result.append(_id)
    return result

def search_and_of_not(dictionary, _01, _02):
    _d1 = search(dictionary, _01)
    _d2 = search_not_of(dictionary, _02)
    return sorted(_and(_d1, _d2))

def search_or_of_not(dictionary, _01, _02):
    _d1 = search(dictionary, _01)
    _d2 = search_not_of(dictionary, _02)
    return sorted(_or(_d1, _d2))


dictionary = get_dictionary()

print(search(dictionary, 'told'))
print(search_and(dictionary, 'dividend', 'Unofficial'))
print(search_or(dictionary, 'oilfield', 'year'))
print(search_and_of_not(dictionary, 'predicted', 'remain'))
print(search_or_of_not(dictionary, 'bank', 'said'))
