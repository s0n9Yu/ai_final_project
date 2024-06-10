import re

tweet = "It seems that #twitter lost some updates yesterday - again!! #twitter #fail"

# 使用正则表达式找到所有的 hashtag
hashtags = re.findall(r'#\w+', tweet)

# 初始化处理后的 tweet
processed_tweet = tweet

# 删除位于句子末尾的 hashtag
for hashtag in reversed(hashtags):
    if processed_tweet.strip().endswith(hashtag):
        processed_tweet = processed_tweet.replace(hashtag, '')
    else:
        processed_tweet = processed_tweet.replace(hashtag, hashtag[1:])

print(processed_tweet.strip())