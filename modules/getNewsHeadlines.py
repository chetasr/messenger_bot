# Powered by https://newsapi.org

# Import essentials

import requests
import json
import os
from pymessenger.bot import Bot
from pymessenger import Element

# Definitons


class getNewsHeadlines:
    # Get news headlines from various news sources
    def __init__(self):
        self.inp = 'news_sources'
        self.out = 'news'

    def do(self, entities):
        r = requests.get('https://newsapi.org/v1/articles', params={
                         'source': entities['news_sources'], 'apiKey': os.environ['NEWSAPI_KEY']})
        data = json.loads(r.text)
        val = []
        for x in data['articles'][:5]:
            elem = Element(title=x['title'], subtitle=x['description'],
                           image_url=x['urlToImage'], item_url=x['url'])
            val.append(elem)
        entities['news'] = ('Here\'s the news', val)
        return entities
