import pandas as pd
import json

file_name = "conversational_chat_response_0"

df = pd.read_csv(f'{file_name}.csv')
with open(f'{file_name}.jsonl', 'w') as f:
    for _, row in df.iterrows():
        json_data = {"prompt": row['prompt'], "completion": row['completion'], 'response': row['response']}
        f.write(json.dumps(json_data) + '\n')

'''
df = pd.read_csv('pronpt_completion.csv')
with open('pronpt_completion_prepared.jsonl', 'w') as f:
    for _, row in df.iterrows():
        json_data = {"prompt": row['prompt'], "completion": row['completion']}
        f.write(json.dumps(json_data) + '\n')


df = pd.read_csv('conversational_chat.csv')
with open('conversational_chat_prepared.jsonl', 'w') as f:
    for _, row in df.iterrows():
        json_data = {"messages": [
            {"role": "system", "content": row['system']}, 
            {"role": "user", "content": row['user']}, 
            {"role": "assistant", "content": row['assistant']}]}
        f.write(json.dumps(json_data) + '\n')
'''