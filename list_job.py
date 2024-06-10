from openai import OpenAI
import config
client = OpenAI(api_key=config.APIKEY)
id = "file-dVdOVNVebjIE1mnpKpeWoBfl"
print(client.fine_tuning.jobs.list(limit=10))