import tweepy
import time

consumer_key = input("enter your consumer key :")
consumer_secret = input ("enter your consumer secret :")
access_token = input (" enter your access token :")
access_token_secret = input ("enter your access token secret :")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()


search = input ("input a search string for tweets")
numberOfTweets = input (" how many tweets would you like to like ? :")

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)


for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        answer=input ("do you want to retweet it(Y/N)? :")
        if answer='Y':
          tweet.retweet()
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
