from chalicelib.mute_words import get_mute_words


def suppresses_users(api, count=200):
    public_tweets = api.home_timeline(count=count)
    mute_words = get_mute_words()

    for tweet in public_tweets:
        if not tweet.retweeted and not tweet.text.startswith('@'):
            for word in mute_words:
                if tweet.text.find(word) != -1:
                    user_id = tweet.user.id_str
                    api.create_mute(user_id=user_id)


def muted_users(api):
    users = [{"name": user.screen_name,
              "id": user.id} for user in api.mutes()]

    return {"users": users,
            "count": len(users)}
