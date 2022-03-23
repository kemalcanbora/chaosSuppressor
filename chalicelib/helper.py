import os
import re


def stop_words_clean(word):
    """
    Remove stop words from a string.
    """
    stop_words = open(os.getcwd()+'/stop-words.txt', 'r').read().split('\n')

    res = re.sub(r'[^\w\s]', '', word)
    words = res.split()

    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

