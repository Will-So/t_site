from flask import Flask, render_template
import json
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("localhost", 27017)
#db = client.tweets


@app.route('/')
def hello_world():
    return render_template('feed.html')


if __name__ == '__main__':
    app.run()
