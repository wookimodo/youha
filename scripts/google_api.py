import pandas as pd
from googleapiclient.discovery import build
import numpy as np
import json
from transformers import pipeline
import re
from html import unescape

def clean_text(text):
    # HTML 태그 제거
    text = re.sub('<[^<]+?>', '', text)
    text = unescape(text)
    
    # 한글, 영어, 공백을 제외한 모든 문자 제거
    text = re.sub('[^ㄱ-ㅣ가-힣a-zA-Z\s]', '', text)
    
    # 공백 제거
    text = text.strip()
    
    return text

# json 파일 저장 함수
def toJson(res_dict,save_name):
    with open(f'{save_name}.json', 'w', encoding='utf-8') as file :
        json.dump(res_dict, file, ensure_ascii=False, indent='\t')
 
# 구글 댓글 google api로 가져오기
api_key = 'AIzaSyBQD_9G1homrY2u9eHQEesEiOOyUEaQn0I'
channel = "딩고 뮤직 / dingo music"
video_id = 'N8mUqh0S80Y'
 
comments = list()
api_obj = build('youtube', 'v3', developerKey=api_key)
response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id, maxResults=100).execute()
 
while response:
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comments.append([comment['textDisplay'], comment['authorDisplayName'], comment['publishedAt'], comment['likeCount']])
 
        if item['snippet']['totalReplyCount'] > 0:
            for reply_item in item['replies']['comments']:
                reply = reply_item['snippet']
                comments.append([reply['textDisplay'], reply['authorDisplayName'], reply['publishedAt'], reply['likeCount']])
 
    if 'nextPageToken' in response:
        response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id, pageToken=response['nextPageToken'], maxResults=100).execute()
    else:
        break
 
df = pd.DataFrame(comments)
# df_length= len(df)
# for i in range(df_length):
#     print(df.iloc[i][1])
# df.to_excel('results.xlsx', header=['comment', 'author', 'date', 'num_likes'], index=None)
 
# 감정분석 모델
classifier = pipeline(
    "sentiment-analysis", model="sangrimlee/bert-base-multilingual-cased-nsmc"
)

result = []
df_length= len(df)
for i in range(df_length):
    comments = clean_text(df.iloc[i][0])
    if comments == "":
        continue
    author  = clean_text(df.iloc[i][1])
    date  = df.iloc[i][2]
    sentiment = classifier(comments)
    result.append([author,comments,date,sentiment[0]['label'],sentiment[0]['score']])
sentiment = pd.DataFrame(result,columns=['author','comment','date','sentiment','score'])

# 감성 분석결과를 json파일로 저장
sentiment_dict = {}
channel_dict = {}
video_dict = {}
length = len(sentiment)

for i in range(length):

    sentiment_dict[i] = {
        'author':sentiment.iloc[i]['author'],
        'comment':sentiment.iloc[i]['comment'], 
        'date':sentiment.iloc[i]['date'],
        'sentiment':sentiment.iloc[i]['sentiment'], 
        'score':sentiment.iloc[i]['score']
                         }
video_dict[video_id] = sentiment_dict
channel_dict[channel] = video_dict

toJson(channel_dict,f"{channel[:2]}_analysis")