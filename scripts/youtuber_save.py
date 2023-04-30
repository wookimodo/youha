from youtuber.models import Youtuber
import json

# Course data
f = open(f'static/data/youtuberData.json', encoding='UTF-8')
youtuberData = json.loads(f.read()) 

def run():

    for i in youtuberData:

        name = youtuberData[i]['name']
        imgUrl = youtuberData[i]['imgUrl']
        link = youtuberData[i]['link']
        subscribers = youtuberData[i]['subscribers']

        Youtuber(name=name, imgUrl=imgUrl, link=link, subscribers=subscribers).save()