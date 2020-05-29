import numpy as np 
import pandas as pd
import re
from pathlib import Path
import time
from tqdm import tqdm

from settings import token
from settings import us_states
from settings import states
from settings import states_abb_dic
from settings import states_full_dic
# data preprocessing
from string import punctuation
from nltk.corpus import stopwords
# sentiment 
from textblob import TextBlob

def main():
    start = time.time()
    data_dirs = ['jsonl/2020-03']
    csv_iterate_dir(data_dirs)
    stop = time.time()
    print("================================================================")
    print("Run time: %f" % (stop-start))


def csv_iterate_dir(data_dirs):
    """
    Iterate jsonl files in each directory
    """
    for data_dir in data_dirs:
        # create a df to store info of cols for each month
        cols = ['id_str', 'created_at', 'state', 'sentiment', 'text_clean']
        
        df_month = pd.DataFrame(columns = cols)
        # list of csv file in current directory
        csv_list = list(Path(data_dir).glob('**/*.csv'))
        print("=============================================================================")
        print("Reading csv files...")
        print("Data preprocessing and sentiment analyzing tweets from csv files...")
        with tqdm(total=len(csv_list)) as pbar:
            for path in csv_list:
                csv_path = path.with_suffix('.csv')
                df = read_csv(path, cols)
                df_month = pd.concat([df_month, df])
                pbar.update(1) 

        # if file does not exist write header 
        with open(str(data_dir+'.csv'), 'a') as f:
            df_month.to_csv(f, mode='a', index=False, header=not f.tell(), encoding='utf-8') 
        
        print("Finished!!!")


def read_csv(path, cols): 
    # 1. load files   
    df = pd.read_csv(path, engine='python')
    # 2. data preprocess
    df = data_preprocess(df)
    # 3. sentiment analysis
    df = sentiment_analysis(df)
    df = df[cols]
    return df

def data_preprocess(df):    
    # Data preprocess
    df['text_clean'] = df['text']
    # lower case
    df['text_clean'] = df['text_clean'].apply(lambda x: str(x).lower())
    # remove unicode
    df['text_clean'] = df['text_clean'].apply(lambda x: remove_unicode(x)) 
    # remove_url
    df['text_clean'] = df['text_clean'].apply(lambda x: remove_url(x))
    # removes hastag in front of a word
    df['text_clean'] = df['text_clean'].apply(lambda x: remove_hashtag(x))
    # removes integers
    df['text_clean'] = df['text_clean'].apply(lambda x: remove_numbers(x))
    # removes emoticons from text
    df['text_clean'] = df['text_clean'].apply(lambda x: remove_emoticons(x))
    # remove punctuation
    df['text_clean'] = df['text_clean'].apply(lambda x: remove_punctuation(x))
    # remove stop words
    df['text_clean'] = df['text_clean'].apply(lambda x: remove_stop_words(x))

    return df

def remove_stop_words(text):
    """Remove stop words"""
    nltk_stop = stopwords.words('english')                                          
    text = ' '.join([c for c in text.split() if c not in nltk_stop]) 
    return text

def remove_unicode(text):
    """ Removes unicode strings like "\u002c" and "x96" """
    text = re.sub(r'(\\u[0-9A-Fa-f]+)',r'', text)       
    text = re.sub(r'[^\x00-\x7f]',r'',text)
    return text

def remove_url(text):
    """ Replaces url address with "url" """
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',text)
    return text    

def remove_hashtag(text):
    """ Removes hastag in front of a word """
    text = re.sub(r'#([^\s]+)', r'\1', text)
    return text

def remove_numbers(text):
    """ Removes integers """
    text = ''.join([i for i in text if not i.isdigit()])         
    return text

def remove_emoticons(text):
    """ Removes emoticons from text """
    text = re.sub(':\)|;\)|:-\)|\(-:|:-D|=D|:P|xD|X-p|\^\^|:-*|\^\.\^|\^\-\^|\^\_\^|\,-\)|\)-:|:\'\(|:\(|:-\(|:\S|T\.T|\.\_\.|:<|:-\S|:-<|\*\-\*|:O|=O|=\-O|O\.o|XO|O\_O|:-\@|=/|:/|X\-\(|>\.<|>=\(|D:', '', text)
    return text

def remove_punctuation(text):
    """remove punctuation"""
    text =  text.translate(str.maketrans('', '', punctuation))
    return text


def sentiment_analysis(df):
    # Sentiment analysis
    # TextBlob stands on the giant shoulders of NLTK and pattern, and plays nicely with both.
    # Here, we only extract polarity as it indicates the sentiment 
    # as value nearer to 1 means a positive sentiment 
    # values nearer to -1 means a negative sentiment. 
    # This can also work as a feature for building a machine learning model.
    df['sentiment_score'] = df['text_clean'].apply(lambda x: TextBlob(x).sentiment[0])
    df['sentiment'] = df['sentiment_score'].apply(lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'neutral')
    df['sentiment_category'] = df['sentiment_score'].apply(lambda x: 1 if x > 0 else 2 if x < 0 else 0)

    return df




if __name__ == '__main__':
    main()