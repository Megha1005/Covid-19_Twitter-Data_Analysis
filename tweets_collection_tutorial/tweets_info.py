import tweepy
from settings import token
from settings import us_states
from settings import states
from settings import states_abb_dic
from settings import states_full_dic
import numpy as np
import pandas as pd
import os
import datetime

class TweetsKeyword():
    def __init__(self, token, keywords, folder, file_name):
        self.token = token
        self.file_name = file_name
        self.keywords = keywords
        self.folder = folder

    def api_token(self, token):
        # Creating the authentication object
        auth = tweepy.OAuthHandler(token['consumer_key'], token['consumer_secret'])
        # Setting your access token and secret
        auth.set_access_token(token['access_token'], token['access_token_secret'])
        # Creating the API object while passing in auth information
        api = tweepy.API(auth)
        return api

    def collect_info(self):
        """
        Finding Tweets Using a Keyword
        """
        #columns of the csv file
        cols = ['screen_name', # user id
                'created_at', # tweet created time
                'location', # location
                'state_abb', # abbreviation of state
                'state',
                'source', # tweet source: phone, web, ...
                'hashtags', 
                'text']
        
        count_tweets = 0 # count total tweets scrapied
        count_pages = 0  # count total pages scrapied

        # tweepy api
        api = self.api_token(self.token)
        
        # foreach through all tweets pulled
        results = tweepy.Cursor(api.search, 
                                q=self.keywords, # The search term you want to find
                                count=100, # count per status page, max/100
                                lang='en', # Language code (follows ISO 639-1 standards)
                                include_rts=False, # rewteets included?
                                wait_on_rate_limit=True, # avoid limits violence, pause for 15min 
                                wait_on_rate_limit_notify=True, # send a notification while reaching rate limit
                                tweet_mode='extended') 

        for page in results.pages():
            # every 100 pages, store as a single file with timeline
            # it would take a long while to read and write a large dataset
            if count_pages % 100 == 0: 
                # under the data folder + time + file name
                file_name = self.folder + '/' + str(datetime.datetime.now().strftime("%Y-%m-%dT%H-%M")) + '_' + self.file_name 
            
            # initial entry dictionary for every page
            new_entry = {i:[] for i in cols}
            
            # collect data
            for status in page:
                # collect location in USA
                location = status.user.location
                if location == None:
                    continue
                # location forms included in us_state in settings
                elif location.split(' ')[-1] not in us_states:
                    continue
                # extract abbreviation of state and state from location
                state_abb, state = self.is_state(location)
                # printing the full text stored inside the tweet object
                try:
                    text = status.retweeted_status.full_text
                except AttributeError:  # Not a Retweet
                    text = status.full_text
                screen_name = status.user.screen_name
                source = status.source
                created_at = status.created_at
                hashtags = ", ".join([t['text'] for t in status.entities['hashtags'] if len(t) > 0])
                print("====================================================")
                print("screen_name: %s" % screen_name)
                print("created_at: %s" % created_at)
                print("location: %s" % location)
                print("source: %s" % status.source)
                print("hashtags: %s" % hashtags)
                print("=======text: \n %s" % text)
                new_entry['screen_name'].append(screen_name)
                new_entry['created_at'].append(created_at)
                new_entry['location'].append(location)
                new_entry['state_abb'].append(state_abb)
                new_entry['state'].append(state)
                new_entry['hashtags'].append(hashtags)
                new_entry['source'].append(source)
                new_entry['text'].append(text)
                count_tweets += 1

            # create a dataframe to add data from current page into it
            df_page = pd.DataFrame(data=new_entry)

            # screen results processing
            count_pages += 1
            print("================================================")
            print("Total pages finished so far: %i" % count_pages)
            print("Total tweets colleted so far: %i" % count_tweets)
            
            # write data into file
            # if file does not exist write header 
            with open(file_name, 'a') as f:
                df_page.to_csv(f, mode='a', header=not f.tell(), columns=cols, index=False, encoding='utf-8')

    def is_state(self, x):
        # return state name and its abbreviation
        for s in x.split(', '):
            if s in states:
                if s in states_abb_dic:
                    return s, states_abb_dic[s]
                else: 
                    return states_full_dic[s], s
                    
        for s in x.split(' '):
            if s in states:
                if s in states_abb_dic:
                    return s, states_abb_dic[s]
                else: 
                    return states_full_dic[s], s

        return np.nan, np.nan