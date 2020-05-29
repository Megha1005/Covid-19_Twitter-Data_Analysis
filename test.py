import pandas as pd


def csv_file():
    df = pd.read_csv('jsonl/2020-01/coronavirus-tweet-id-2020-01-31-22.jsonl.csv')
    print(df.info())

def main():
    csv_file()

if __name__ == '__main__':
    main()