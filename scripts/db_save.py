from youtuber.models import Youtuber, Comment
import json

# json 파일 불러오기
f = open(f'static/data/youtuberData.json', encoding='UTF-8')
youtuberData = json.loads(f.read()) 

f = open(f'static/data/commentData.json', encoding='UTF-8')
comments = json.loads(f.read()) 

def run():

    # Youtuber Table 저장
    for i in youtuberData:

        name = youtuberData[i]['name']
        imgUrl = youtuberData[i]['imgUrl']
        link = youtuberData[i]['link']
        subscribers = youtuberData[i]['subscribers']

        Youtuber(name=name, imgUrl=imgUrl, link=link, subscribers=subscribers).save()

    channelDict = {"1MILLION Dance Studio":"WGG-0oJOIxE", "DONA 도나":"YqV8_4i5MRc", "딩고 뮤직 / dingo music":"N8mUqh0S80Y", "Jane ASMR 제인":"DTkT6ToYwgc"}

    # Comment Table 저장
    for (channel,video) in channelDict.items():

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