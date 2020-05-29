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

def main():
    text_clean()

def text_clean():    

    input_text = "We're Staying Unified In The Fight Against COVID 19! 😁 Salute To @naviomusic For His Contribution To The National Taskforce & For Supporting Fellow Ugandans.Read Review To His New Album 'Strength In Numbers' Here ~ https://bit.ly/2T42YGi #SINalbum #StrengthInNumbers #UGHipHop"
    text_c = str(input_text).lower()
    print(text_c)
    text_c = remove_stop_words(text_c)
    text_c = remove_unicode(text_c)
    text_c = remove_url(text_c)
    text_c = remove_hashtag(text_c)
    text_c = remove_numbers(text_c)
    text_c = remove_emoticons(text_c)
    text_c = remove_punctuation(text_c)

    print(text_c)


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


if __name__ == '__main__':
    main()