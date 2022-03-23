from chalicelib.mute_words import get_mute_words
from chalicelib.helper import stop_words_clean
from collections import Counter
from itertools import takewhile
import tweepy


def suppresses_users(api, count=75, threshold=3, users_last_n_tweets=10):
    public_tweets = api.home_timeline(count=count)
    mute_words = get_mute_words()
    following_list = api.friends_ids(user_id=api.me().id)

    for tweet in public_tweets:
        if not tweet.retweeted and not tweet.text.startswith('@'):
            for word in mute_words:
                if tweet.text.find(word) != -1:
                    user_id = tweet.user.id_str
                    if user_id not in following_list:
                        tweets_list = api.user_timeline(user_id=user_id,
                                                        count=users_last_n_tweets,
                                                        tweet_mode='extended')
                        user_tweet_corpus = [stop_words_clean(tweet.full_text.lower()) for tweet in tweets_list]

                        words = []
                        for t in user_tweet_corpus:
                            words.extend(t.split())

                        more_than_threshold = dict(takewhile(lambda i: i[1] >= threshold, Counter(words).most_common()))

                        if any(x in list(more_than_threshold.keys()) for x in mute_words):
                            print(f"{user_id} {tweet.text} is banned!")
                            api.create_mute(user_id=user_id)


def muted_users(api):
    mutes = []
    for page in tweepy.Cursor(api.mutes, count=200).pages():
        for user in page:
            mutes.append({"screen_name": user.screen_name, "id": user.id})

    return {"users": mutes,
            "count": len(mutes)}
