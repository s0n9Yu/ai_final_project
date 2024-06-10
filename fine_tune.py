from openai import OpenAI
import config

client = OpenAI(api_key=config.APIKEY)

ID = client.files.create(
  file=open("pronpt_completion_prepared.jsonl", "rb"),
  purpose="fine-tune"
).id

print(ID)

client.fine_tuning.jobs.create(
  training_file=ID, 
  model="babbage-002"
)
