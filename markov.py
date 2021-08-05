"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text = open('green-eggs.txt').read()
    #print(text)
    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
        #dictionary[(word1, word2)] = value
        value = []

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = text_string.split()

    for i in range(len(words) - 2):
        tup_for_diction = (words[i], words[i + 1])
        key = tup_for_diction
        value = words[i + 2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    key = choice(list(chains.keys()))
    print('****')
    words = choice(chains[key])
    print(choice(key))
    print(key)
    print(words)
    
    while words:
        words = choice(chains[key])
    
    i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
    return ' '.join(words)

    random.choice(words)

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
