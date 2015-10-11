from flask import Flask
import json

app = Flask(__name__)


@app.route('/feed')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
