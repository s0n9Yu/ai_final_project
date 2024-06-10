import openai
from openai import OpenAI
import json
import pandas as pd
from tqdm import tqdm
import config

openai.api_key = config.APIKEY
client = OpenAI(api_key=config.APIKEY)
model = config.FINETUNED_MODEL # model name after fine-tuning

system_prompt = "please give at least one hashtags of the following tweet and answer with hashtags only: "

# modify this to the input of the model
user_prompt = "The  The Last Word felt like a total waste of time. The story was weak as were the characters and it had no resolution what so ever"

end_separater = "  ->"

prompt = system_prompt + user_prompt + end_separater

response = openai.completions.create(
    model=model,
    prompt=prompt
)
parse_out = response.choices[0].text

print("prompt: ", prompt)
print("responce: ", parse_out)