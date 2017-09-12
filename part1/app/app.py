#!/usr/bin/python3.5
from flask import Flask, jsonify, abort, make_response, request
from redis import Redis
import socket

host = socket.gethostname()

app = Flask(__name__)
redis_db = Redis(host='redis', port=6379)

@app.route('/ping')
def ping():
    answers = {
        "status": "ok",
        "server": host
    }
    redis_db.incr('hits')
    return jsonify({'Answer': answers})

@app.route('/total')
def total():
    total = redis_db.get('hits')
    if total != 0:
        answers = {
                "status": "ok",
                "total": total.decode('utf-8')
            }
    else:
        answers = {
                "status": "okok",
                "total": "0"
            }
    return jsonify({'Answer': answers})

@app.route('/reset')
def reset():
    redis_db.set('hits', 0)
    return "Reset value" 

@app.route('/test')
def test():
    return "Test OK"    


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

