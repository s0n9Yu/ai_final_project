import openai
from openai import OpenAI
import json
import pandas as pd
from tqdm import tqdm
import time

import sys
sys.path.append('../')
import config

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--index", type=int, default=3)
args = parser.parse_args()

index = args.index
print(f"index: {index}\n")

apikey = [
    config.APIKEY,
    config.APIKEY,
    config.APIKEY,
    config.APIKEY
]

client = OpenAI(api_key=apikey[index]) #new1

df = pd.read_csv(f'conversational_chat_{index}.csv')
responses = []
for prompt in tqdm(df['user']):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "please give at least one hashtags of the following tweet and answer with hashtags only without starting with #, separated with comma: "},
            {"role": "user", "content": prompt}
        ]
    )
    answer = response.choices[0].message.content.strip()
    answer = answer.replace('#', '').strip()
    responses.append(answer)
    time.sleep(0.5)

df['response'] = responses
df.to_csv(f'conversational_chat_response_{index}.csv', columns=['system', 'user', 'assistant', 'response'])
