from flask import Flask
from flask_caching import Cache

app1 = Flask(__name__)
cache1 = Cache(
    app1,
    config={
        'CACHE_TYPE': 'redis',
        'CACHE_REDIS_HOST': '123.57.148.207',
        'CACHE_REDIS_PORT': 6379,
    }
)
cache1.init_app(app1)
if __name__ == '__main__':
    cache1.set("955650e200c24e7db0e65d9c7572e28f","20",60*60)
    print("set success")
    c = cache1.get('955650e200c24e7db0e65d9c7572e28f')
    print(c)