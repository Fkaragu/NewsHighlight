from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_source, get_article


#  views
@main.route('/')
def index():
	'''
	function returns index page and its data
	'''

	news_sources = get_source('sources')
	news_articles = get_article('articles')

	return render_template('index.html',sources = news_sources)
