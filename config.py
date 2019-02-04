import os

class Config:
  '''
  general configaration class
  '''
  NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?language=en&apiKey={}'
  NEWS_API_KEY = 'ec8d248df3204bd999e2821ee4bbee57'
  NEWS_API_BASE_URL2 = 'https://newsapi.org/v2/top-headlines?language=en&apiKey={}'

#   top-headlines?language=en
#   NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?apiKey={}'
#   NEWS_API_KEY = 'ec8d248df3204bd999e2821ee4bbee57'



# https://newsapi.org/v2/sources?apiKey=ec8d248df3204bd999e2821ee4bbee57
# https://newsapi.org/v2/top-headlines?sources=cnn&apiKey=ec8d248df3204bd999e2821ee4bbee57


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
