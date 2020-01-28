class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'

class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config:The parent configuartion class with General configuration setting
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration class
    
    Args:
        Config:The parent configuration class with the General configuration settings
    '''
    
    DEBUG = True
