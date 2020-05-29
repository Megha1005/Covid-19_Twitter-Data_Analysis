# Source
# https://chatbotslife.com/twitter-data-mining-a-guide-to-big-data-analytics-using-python-4efc8ccfa219


import tweepy
from settings import token
from settings import us_states
import numpy as np
import pandas as pd
import os

def my_info(api):
    """
    Example 1: Your Timeline
    """


    # Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
    public_tweets = api.home_timeline()
    # foreach through all tweets pulled
    for tweet in public_tweets:
       # printing the text stored inside the tweet object
       print(tweet.text)
       print(tweet.user.screen_name)
       print(tweet.user.location)


def specifit_user(api):
    """
    Example 2: Tweets from a Specific User
    """

    # The Twitter user who we want to get tweets from
    name = "nytimes"
    # Number of tweets to pull
    tweetCount = 20
    # Calling the user_timeline function with our parameters
    results = api.user_timeline(id=name, count=tweetCount)
    # foreach through all tweets pulled
    for tweet in results:
        # printing the text stored inside the tweet object
        print(tweet.text)
        print(tweet.user.screen_name)
        print(tweet.user.location)



def keywords(api):
    """
    Example 3: Finding Tweets Using a Keyword
    """
    
    #columns of the csv file
    cols = ['screen_name', 'created_at', 'location', 'source', 'hashtags', 'text']
    
    count_tweets = 0 # count total tweets scrapied
    count_pages = 0  # count total pages scrapied

    # foreach through all tweets pulled
    results = tweepy.Cursor(api.search, 
                            q='COVID-19', # The search term you want to find
                            count=100, # count per status page, max/100
                            lang='en', # Language code (follows ISO 639-1 standards)
                            include_rts=False, # rewteets included?
                            wait_on_rate_limit=True, # avoid limits violence 
                            since='2020-04-01',
                            # geocode = '37.781157, -122.398720, 1mi', # area coordicates 19.50139 to 64.85694 and longitude from -161.75583 to -68.01197
                            tweet_mode='extended') 
    
    for page in results.pages():
        new_entry = {
            'screen_name': [], 
            'created_at': [], 
            'location': [], 
            'source': [], 
            'hashtags': [], 
            'text': []
            }
        # collect data
        for status in page:
            count_tweets += 1
            print("====================================================")
            # printing the full text stored inside the tweet object
            try:
                text = status.retweeted_status.full_text
            except AttributeError:  # Not a Retweet
                text = status.full_text
            # collect USA based
            location = status.user.location
            if location == None:
                continue
            elif location.split(' ')[-1] not in us_states:
                continue

            screen_name = status.user.screen_name
            source = status.source
            created_at = status.created_at
            hashtags = ", ".join([t['text'] for t in status.entities['hashtags'] if len(t) > 0])
            
            print("text: \n %s" % text)
            print("source: %s" % status.source)
            print("screen_name: %s" % screen_name)
            print("location: %s" % location)
            print(location.split(' '))
            print(location.split(' ')[-1])

            print("created_at: %s" % created_at)
            print("hashtags: %s" % hashtags)
            # print(status)
            new_entry['screen_name'].append(screen_name)
            new_entry['created_at'].append(created_at)
            new_entry['location'].append(location)
            new_entry['hashtags'].append(hashtags)
            new_entry['source'].append(source)
            new_entry['text'].append(text)
        count_pages += 1
        print("================================================")
        print("Total pages finished so far: %i" % count_pages)
        print("Total tweets colleted so far: %i" % count_tweets)

def main():
    # Creating the authentication object
    auth = tweepy.OAuthHandler(token['consumer_key'], token['consumer_secret'])
    # Setting your access token and secret
    auth.set_access_token(token['access_token'], token['access_token_secret'])
    # Creating the API object while passing in auth information
    api = tweepy.API(auth)

    keywords(api)


if __name__ == '__main__':
    main()
























