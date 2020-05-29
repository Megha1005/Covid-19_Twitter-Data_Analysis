from read_csv import csv_iterate_dir
from read_jsonl import jsonl_iterate_dir
from unzip_gz import unzip_gz


def main():
    # change to the target data_dirs
    data_dirs = ['jsonl/2020-01', 'jsonl/2020-02', 'jsonl/2020-03', 'jsonl/2020-04', 'jsonl/2020-05']
    gz_jsonl_csv_df(data_dirs)

def gz_jsonl_csv_df(data_dirs):
    for d in data_dirs:
        print("At folder: ", d)
        # 1. upzip gz files to jsnol
        unzip_gz([d])
        # 2. extract tweets from jsonl files and store as csv
        jsonl_iterate_dir([d])
        # 3. read tweets from csv files, data preprocessing and snetiment analysis
        # store as pandas and combine them single csv file
        csv_iterate_dir([d])


if __name__ == '__main__':
    main()