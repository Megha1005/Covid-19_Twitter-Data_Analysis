from settings import token
from tweets_info import TweetsKeyword


def main():
    # api token
    api_token = token
    # write in to file
    file_name = 'tweets-covid-19.csv'
    # folder to store your collected data
    folder = 'test_data'
    # search keyword
    keywords = ['COVID']
    tweets = TweetsKeyword(api_token, keywords, folder, file_name)
    tweets.collect_info()

if __name__ == '__main__':
    main()