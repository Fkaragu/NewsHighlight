from flask import render_template,request,redirect,url_for
from app import app
import urllib.request
import json

news_api ='ec8d248df3204bd999e2821ee4bbee57'

#CNN
url_cnn = 'https://newsapi.org/v2/top-headlines?sources=cnn&apiKey='+ news_api
json_obj_cnn = urllib.request.urlopen(url_cnn)
data_cnn = json.load(json_obj_cnn)

#AL-JAZEERA
url_ALJ = 'https://newsapi.org/v2/top-headlines?sources=al-jazeera-english&apiKey='+ news_api
json_obj_ALJ = urllib.request.urlopen(url_ALJ)
data_ALJ = json.load(json_obj_ALJ)

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/cnn')
def cnn():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('cnn.html', data_cnn = data_cnn)

@app.route('/aljazeera')
def aljazeera():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('aljazeera.html', data_ALJ = data_ALJ)
