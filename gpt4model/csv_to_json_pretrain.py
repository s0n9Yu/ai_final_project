import pandas as pd
import json

file_name = "conversational_chat_response_3"

df = pd.read_csv(f'{file_name}.csv')
with open(f'{file_name}.jsonl', 'w') as f:
    for _, row in df.iterrows():
        json_data = {"prompt": str(row['system'])+str(row['user']), "completion": row['assistant'], 'response': row['response']}
        f.write(json.dumps(json_data) + '\n')
