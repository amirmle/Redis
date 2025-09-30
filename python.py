import redis 
import json

redis_host = 'localhost'
redis_port = 6379
redis_pass = 123
redis_db = 8
rd = redis.Redis(host=redis_host, port=redis_port, password=redis_pass, db=redis_db)

# rd.set('username', 'new amir')
# rd.set('email', 'amir@gmail.com')

# email = rd.get('email')
# print(email)

with open('persons.json') as p :
    data = json.load(p)
    
with rd.pipeline(data) as pipe :
    for id, person in enumerate(data, start=1) :
        pipe.hsetnx('persons', id , str(person))
    pipe.execute()
