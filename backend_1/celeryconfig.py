# celeryconfig.py
BROKER_URL = 'redis://localhost:6379'
# Result backend URL for storing task results
#CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'
# Redis URL for caching
REDIS_URL = 'redis://localhost:6379'
# Additional Celery configurations
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'UTC'

# Additional Flask configurations
CACHE_TYPE = 'RedisCache'
CACHE_DEFAULT_TIMEOUT = 300
CACHE_REDIS_HOST = 'localhost'
CACHE_REDIS_PORT = 6379
CACHE_REDIS_DB = 9
