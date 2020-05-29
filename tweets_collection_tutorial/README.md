## 1. Tweets Collecting Tutorial
Tutorial of Collecting Tweets with Tweets' API

## 1.1 Examples
Under the file
**[tweets_api_eg.py](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/tweets_collection_tutorial/tweets_api_eg.py)**

There are three examples of collecting tweets:
- Example 1: Your Timeline
- Example 2: Tweets from a Specific User
- Example 3: Finding Tweets Using a Keyword

## 1.2 Collect data
### 1.2.1 Set up API key
- In the **[settings.py](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/settings.py)**, you can use your own token.

    - **[Twitter Data Mining: A Guide to Big Data Analytics Using Python](https://chatbotslife.com/twitter-data-mining-a-guide-to-big-data-analytics-using-python-4efc8ccfa219)** is a tutorial of how to apply for a developer ID and how to utilize it. 
    
### 1.2.2 Set up argument in main file
- Main class. In the python file **[main.py](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/tweets_collection_tutorial/main.py)**, set parameters `api token`, `folder`, `file name`, and `keywords`. Run `main.py` to collect tweets with keywords.
```
# api token
api_token = token
# write in to file
file_name = 'tweets-covid-19.csv'
# folder to store your collected data
folder = 'test_data'
# search keyword
# 'COVID-19', 'COVID19', 'Covid_19', 'CoronavirusPandemic', 'CoronavirusOutbreak','CoronaVirusUpdate'
keywords = ['COVID']
```

- **[tweets_info.py](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/tweets_collection_tutorial/tweets_info.py)** is a Python class to collect tweets

    - Columns we will collect, change the `cols` in  `tweets_info.py` to get more information from each single tweet.
    ```
    #columns of the csv file
    cols = ['screen_name', # user id
            'created_at', # tweet created time
            'location', # location
            'state_abb', # abbreviation of state
            'state',
            'source', # tweet source: phone, web, ...
            'hashtags', 
            'text']
    ```