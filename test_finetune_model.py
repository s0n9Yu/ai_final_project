import openai
from openai import OpenAI
import json
import pandas as pd
from tqdm import tqdm
import config

openai.api_key = config.APIKEY
client = OpenAI(api_key=config.APIKEY)
model = config.FINETUNED_MODEL

data = []
with open('pronpt_completion_prepared.jsonl', 'r') as f:
    for line in tqdm(f):
        json_data = json.loads(line.strip())
        data.append(json_data)

df = pd.DataFrame(data)
responses = []
for prompt in tqdm(df['prompt']):
    response = openai.completions.create(
        model=model,
        prompt=prompt
    )
    parse_out = response.choices[0].text
    responses.append(parse_out)

df['response'] = responses
df.to_csv('pronpt_completion_response.csv', columns=['prompt', 'completion', 'response'])