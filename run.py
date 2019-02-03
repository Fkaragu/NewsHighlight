#!/usr/bin/env python

import urllib.request
import json

news_api ='ec8d248df3204bd999e2821ee4bbee57'

url = 'https://newsapi.org/v2/top-headlines?sources=cnn&apiKey='+ news_api
json_obj = urllib.request.urlopen(url)

data = json.load(json_obj)



print(data)
