import warnings
from tqdm import tqdm
import pandas as pd
import re

warnings.filterwarnings("ignore")

instruction = 'please give at least one hashtags of the following tweet and answer with hashtags only: '
tail = '  ->'
prompt = []
user = []
completion = []
assistant = []
total_df_pronpt_completion = None
total_df_conversational_chat = None
df = pd.read_csv('tweet_tag.csv')
for tag_str in df['hashtag']:
    assistant.append(tag_str)
    tag_str = re.sub('#', '', tag_str)
    completion.append(tag_str)
for tweet in df['tweet']:
    tags = re.findall(r'#\w+', tweet)
    tweet_without_tag = re.sub(r'#\w+', '', tweet)
    user.append(tweet_without_tag)
    prompt.append(instruction + tweet_without_tag + tail)
data_prompt_completion = {'prompt': prompt, 'completion': completion}
data_conversational_chat = {'system': instruction, 'user': user, 'assistant': assistant}
df_pronpt_completion = pd.DataFrame(data_prompt_completion)
df_conversational_chat = pd.DataFrame(data_conversational_chat)
total_df_pronpt_completion = df_pronpt_completion
total_df_conversational_chat = df_conversational_chat

total_df_pronpt_completion.to_csv('pronpt_completion.csv', columns=['prompt', 'completion'])
total_df_conversational_chat.to_csv('conversational_chat.csv', columns=['system', 'user', 'assistant'])