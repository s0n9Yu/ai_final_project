import flask
from flask import request, jsonify
import openai
from openai import OpenAI
import json
import pandas as pd
from tqdm import tqdm

import sys
sys.path.append('../')
import config

from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

client = OpenAI(api_key=config.APIKEY)

system_prompt = "please give at least one hashtags of the following tweet and answer with hashtags only: "

end_separater = "  ->"

@app.route("/")
@app.route("/hello")
def hello():
    return "Hello, World!"
@app.route("/query", methods=['POST'])
def query():
    user_prompt = request.form.get('query')
    print(user_prompt)
    prompt = system_prompt + user_prompt + end_separater

    response = client.chat.completions.create(
        model=config.PRETRAINED_MODEL,
        messages=[
            {"role": "system", "content": "please give at least one hashtags of the following tweet and answer with hashtags only without starting with #, separated with comma: "},
            {"role": "user", "content": prompt}
        ]
    )
    logit = response.choices[0].message.content.strip()
    logit = logit.replace('#', '').strip()
    logit = str(logit).split(',')
    logit = [s.lower().strip() for s in logit]
    return jsonify({"result": logit})
    

if __name__ == '__main__':
    app.run()