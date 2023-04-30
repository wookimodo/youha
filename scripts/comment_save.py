from youtuber.models import Youtuber, Comment
import json

# Course data
f = open(f'static/data/딩고_analysis.json', encoding='UTF-8')
comments = json.loads(f.read()) 

def run():

    channel = "딩고 뮤직 / dingo music"
    video = "N8mUqh0S80Y"
    comments_len = len(comments[channel][video])

    for i in range(comments_len):

        i = str(i)

        videoId = video
        author = comments[channel][video][i]['author']
        comment = comments[channel][video][i]['comment']
        date = comments[channel][video][i]['date']
        sentiment = comments[channel][video][i]['sentiment']
        score = comments[channel][video][i]['score']

        Comment(name_id = Youtuber.objects.get(name=channel).pk, videoId=videoId, author=author, comment=comment, date=date, sentiment=sentiment, score=score).save()