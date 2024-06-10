import jsonlines
import tqdm
import re

file_name = "pronpt_completion_response.jsonl"

tag_count = 0
tag_recall = 0
test_count = 0
prompt_len_avg = 0
prompt_len_max = float("-inf")
prompt_len_min = float("inf")

with open(file_name, 'rb') as f:
    for items in tqdm.tqdm(jsonlines.Reader(f)):
        prompt_len_avg += len(items['prompt'])
        prompt_len_max = max(prompt_len_max, len(items["prompt"]))
        prompt_len_min = min(prompt_len_min, len(items["prompt"]))
        test_count += 1
        ground_truth = items['completion'].split(',')
        ground_truth = [s.lower().strip() for s in ground_truth]
        logit = str(items['response']).split(',')
        logit = [s.lower().strip() for s in logit]
        tag_count += len(ground_truth)
        for gt in ground_truth:
            if gt in logit:
                tag_recall += 1
        
prompt_len_avg = prompt_len_avg / test_count        

print("\n--------------\n")
print("test_count: ", test_count)
print("prompt_len_avg: ", prompt_len_avg)
print("prompt_len_min: ", prompt_len_min)
print("prompt_len_max: ", prompt_len_max)
print("tag_count: ", tag_count)
print("tag_recall: ", tag_recall)
print("recall: ", tag_recall / tag_count * 100.0 , "%")