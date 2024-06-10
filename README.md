# ai_final_project

## Introduction
Our goal is to create an automatic pipeline to generate tags from a given content. The input of the pipeline is the texts that users want to generate keywords, and the output is some tags(keywords) that are related to the texts.

## Setup

### unzip large files
```
$ unzip largefiles.zip
$ cd gpt4model
$ unzip largefiles.zip
```
### environment
```
$ pip install -r requirements.txt
```
### api key
Fill in the OpenAI api key in config.py:
```
APIKEY = "<your key>"
```

## Usage

### Run backend
```
$ cd backend
$ python3 main.py
```

### Run frontend
```
$ cd frontend
$ npm start
```
### Run metric
Fill in the output file in file_name of metric.py
```
$ python3 metric.py
```
### Fine-tune model
```
$ python3 fine_tune.py
```
Then you will get a model name like "ft:babbage-002:personal::9XnUUG89" in the website of openai api page, then update the FINETUNED_MODEL in config.py

Then we can run the following to test it in the dataset:
```
$ python3 test_finetune_model.py
```

### GPT4-based model
In addition to interactively input the prompt, we test the dataset by the following commands,
```
$ cd gpt4model
$ python3 test_gpt4.py --index {0,1,2,3}
```
Then the output file can be used to run metric.