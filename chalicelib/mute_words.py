import urllib.request
import os


def get_mute_words():
    with urllib.request.urlopen(os.environ["MUTE_LIST_URL"]) as response:
        mute_words = response.read().decode('utf-8')
    return eval(mute_words)

