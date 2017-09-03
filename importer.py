import redis

r = redis.StrictRedis(
    host='localhost',
    port=6379,
    db=0,
    password='0xJHtqj7wHlWQVm5Kjfepbk2UApdMQke')


f = open('/Users/jicowan/Downloads/products_list.txt',"r")
for line in f:
    n = line.strip()
    for l in range(1,len(n)):
        prefix = n[0:l]
        r.zadd('autocomplete',0,prefix)
    r.zadd('autocomplete',0,n+"%")
else:
    exit