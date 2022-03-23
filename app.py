from chalice import Chalice, Rate
from chalicelib import suppressor
import tweepy
import os

app = Chalice(app_name='chaosSuppressor')
auth = tweepy.OAuthHandler(os.environ["TWITTER_CONSUMER_KEY"], os.environ["TWITTER_CONSUMER_SECRET"])
auth.set_access_token(os.environ["TWITTER_ACCESS_TOKEN"], os.environ["TWITTER_ACCESS_TOKEN_SECRET"])
api = tweepy.API(auth)


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/list', methods=['GET'])
def muted_user_list():
    return suppressor.muted_users(api)


@app.schedule(Rate(15, unit=Rate.MINUTES))
def suppresses_lambda(event):
    suppressor.suppresses_users(api)
