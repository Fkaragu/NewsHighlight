import os

class Config:
  '''
  general configaration class
  '''
  NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?language=en&apiKey={}'
  NEWS_API_KEY = 'ec8d248df3204bd999e2821ee4bbee57'
  NEWS_API_BASE_URL2 = 'https://newsapi.org/v2/everything?sources=bbc-news,al-jazeera-english,cnn,independent,google-news,the-telegraph,mashable,the-lad-bible,buzzfeed,bloomberg,engadget,espn,fortune&sortBy=publishedAt&pageSize=100&apiKey={}'


class ProdConfig(Config):
    '''
    production configuration class
    '''
    pass


class DevConfig(Config):
    '''
    development configuration class
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
