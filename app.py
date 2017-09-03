from flask import Flask, jsonify, request
import redis

app = Flask(__name__)

@app.route('/todo', methods=['GET'])

def get_query():
    r = redis.StrictRedis(host=redis-master, port=6379, db=0, password=$REDIS_PASSWORD)
    count = 50
    results = []
    grab = 42
    prefix = request.args.get('query')
    start = r.zrank('autocomplete', prefix)
    if not start:
        return []
    while (len(results) != count):
        range = r.zrange('autocomplete', start, start + grab - 1)
        start += grab
        if not range or len(range) == 0:
            break
        for entry in range:
            minlen = min(len(entry), len(prefix))
            if entry[0:minlen] != prefix[0:minlen]:
                count = len(results)
                break
            if entry[-1] == "%" and len(results) != count:
                results.append(entry[0:-1])
    return jsonify({'results': results})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
