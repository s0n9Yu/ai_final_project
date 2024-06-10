import warnings
from tqdm import tqdm
import pandas as pd
import re

warnings.filterwarnings("ignore")

total_df_with_tag = None
total_df_without_tag = None
chunksize = 10000
count = 1
for df in pd.read_csv('./archive/training.1600000.processed.noemoticon.csv', chunksize=chunksize):
    #print(count)
    #if count > 5:
    #    break
    tag_index = []
    no_tag_index = []
    hashtag_list = []
    for (i, tweet) in enumerate(df['tweet']):
        if '#' not in tweet:
            no_tag_index.append(i + (count - 1) * chunksize)
        else:
            tags = re.findall(r'#\w+', tweet)
            if tags == []:
                no_tag_index.append(i + (count - 1) * chunksize)
            else:
                tag_index.append(i + (count - 1) * chunksize)
                tag_str = ','.join(tags)
                hashtag_list.append(tag_str)
    tag_df = df.drop(no_tag_index)
    no_tag_df = df.drop(tag_index)
    tag_df['hashtag'] = hashtag_list
    if count == 1:
        total_df_with_tag = tag_df
        total_df_without_tag = no_tag_df
    else:
        total_df_with_tag = pd.concat([total_df_with_tag, tag_df], join='inner')
        total_df_without_tag = pd.concat([total_df_without_tag, no_tag_df], join='inner')
    count += 1

total_df_with_tag.to_csv('tweet_tag.csv', columns=['tweet', 'hashtag'])
total_df_without_tag.to_csv('tweet.csv', columns=['tweet'])