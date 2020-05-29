# COVID-19_Tweets-analysis
The pandemic of coronavirus has got all the countries over the world to review their existing strategies. The conventional methods of research in science are in need of an upgrade. In this era of data explosion, the spread of this pandemic has led to an even more huge contribution to data in every aspect, not just medical. Coronavirus has affected all the fields of humanity at every level, ranging from daily-life of a layman to working of gigantic establishments globally. Hence, there is a huge obligation of fulfilling the need for useful information and real solutions. So the data researchers have tirelessly been working on the raw real-time data to understand why and how COVID-19 spreads and kills, how is the recovery, how is the common population contributing in its spread or control and to what extent, how fast is the information spreading on it let it be valid or false. All these points are very necessary to be addressed and the running of most of the high percentage of worldwide tasks depend on this analysis. Hence, as we were provided the opportunity to be a part of this analysis, we decided to work on the data available from twitter on COVID-19.

## Enviroment Setup
- (Python 2) Run `pip install -r requirements.txt`
- (Python 3) Run `pip3 install -r requirements.txt`

## 1. Data Collection
### 1.1 Worldometer dataset
Run **[GetData_USA.py](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/Data_Collection/GetData_USA.py)** to scripy the data from **[worldometers.info](worldometers.info)**


### 1.2 Tweets dataset
#### 1.2.1 General Tweets Collecting Tutorial
In the subfolder of **[tweets_collecting_tutorial](https://github.com/AllenSun7/COVID-19_Tweets-analysis/tree/master/tweets_collection_tutorial)** 
- 1.1 Examples: there are three examples of collecting tweets:
    - Example 1: Your Timeline
    - Example 2: Tweets from a Specific User
    - Example 3: Finding Tweets Using a Keyword
- 1.2 Collect data   
    - 1.2.1 Set up API key
    - 1.2.2 Set up argument in main file

#### 1.2.2 Collect data 
Data was collected by filtering the original dataset under the repository of **[COVID-19-TweetIDs](https://github.com/echen102/COVID-19-TweetIDs)** which contains collected tweets IDs associated with the novel coronavirus COVID-19.
The original dataset contains Tweets’ ids dating from January 22th, 2020 to May 8th, 2020 with 101,718,655 tweets. 

Used the tool Hydrator to rehydrate the tweet-IDs i.e. to fetch tweets data related to the tweet-IDs using Twitter’s API. 

Run the **[extrac_tweets.py](https://github.com/AllenSun7/COVID-19_Tweets-analysis/tree/master/extrac_tweets.py)** 

Filtered the location in the US only by the list in Appendix A. Extracted the attributes of id_str, created_at, location, and text of each tweet and features are categorical values following the steps below:

- 1). Hydrate the tweet-IDs and store them as .gz files.
- 2). Unzip the .gz files to .jsonl files
- 3). Extract relevant tweets and features from .jsonl files and store them as .csv files
- 4). Concatenate all .csv files into separate months.
Eventually, 15,099,967 tweets were collected, and the size of the dataset dropped from 1TB to 3GB. 

|Tweets Type            |Number of tweets   |Size of dataset  |
|-------------          |----------------   |---------------  |
| Original dataset      | 101,718,655       |   1 TB          |
| Filtered dataset      |  15,099,967       |   3 GB          |
| Preprocessed dataset  |  14,067,351       | 2.5 GB          |



## 2. Data Preprocess
- Worldometer
Dropping useless columns 
- Twitter data 
    1. Converting the locations to state
    2. Text preprocessing technicks in the **[read_csv.py](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/read_csv.py)**

        - Lower case
        - Remove URL address
        - Remove Unicode
        - Remove stop words
        - Remove hashtag 
        - Remove integers
        - Remove emoticons
        - Remove punctuation
    

    3. Removing missing values
- Merging twitter and worldometer data chronologically
Run **[data_output.py](https://github.com/AllenSun7/COVID-19_Tweets-analysis/tree/master/data_output.py)** to output more related csv files, which are stored in **[src](https://github.com/AllenSun7/COVID-19_Tweets-analysis/tree/master/src)**

**[COVID-19_Tweets-analysis_Dataset](https://drive.google.com/drive/folders/1eldqmOJw-LYUw5HvRDCMxnH-ZU48cqkE?usp=sharing)** is the dataset for 5 months after being preprocessed.


## 3. Data Visualization
### 3.1 Basic data visualization
Basic data visualization in the file of **[data_visualization.ipynb](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/data_visualization.ipynb)**
    <!-- - Daily Tweets -->
    <img src="https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/src/daily_tweets.png"/>
    <!-- - Total Tweets for each state -->
    <img src="https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/src/tweets_states.png"/>
    <!-- - Word Cloud  -->
    <img src="https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/src/tweets_wordcloud.png" width="800" height="700"/>

### 3.2 Heatmap 
Heatmap in the file of **[heatmap.ipynb](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/heatmap.ipynb)**
    <!-- - Tweets Heatmap  -->
    <img src="https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/src/heatmap_tweets.png"/>
    <!-- - Cases Heatmap -->
    <img src="https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/src/heatmap_cases.png"/>

## 4. Algorithms
Four models implemented for sentiment analysis with Groud Truth by randomly obtaining 100 tweets from dataset: 

- Afinn
- Vader
- TextBlob
- SentiStrength
- Ensemble

Run **[SentiStrengthGroundtruth.ipynb](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/SentiStrengthGroundtruth.ipynb)** for the model of SentiStrength
Run **[Vader-Afinn-Ensemble_F1-score.ipynb](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/Vader-Afinn-Ensemble_F1-score.ipynb)** to evaluate the models obove.
Results:
<img src="https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/src/evalutions.png" width="500" height="200"/>

F1-score order: Afinn > Vader  > Ensemble > sentistrength> TextBlob

## 5. Correlation
Afinn dominats the models, it is applied to analyze each tweet.
<!-- - sentiments_tweets  -->
<img src="https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/src/sentiments_tweets.png"/>
<!-- - sentiments_cases -->
<img src="https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/src/sentiments_cases.png"/>
<!-- - tweets_cases -->
<img src="https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/src/tweets_cases.png"/>




## Knowledge Discover(KDD) Process - check list
- [x]  1) data cleaning
- [x]  2) data integration
- [x]  3) data selection
- [x]  4) transformation
- [x]  5) data mining
- [x]  6) pattern evaluation 
- [x]  7) knowledge presentation

## Notes
- Rate Limit.
    - wait_on_rate_limit. Whether or not to automatically wait for rate limits to replenish. Rate limits are divided into 15 minute intervals.  
    - Total Requests Limit. For each free API key, there is a limit for monthly requests: up tp 250. 
