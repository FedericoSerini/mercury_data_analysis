from flask import Flask
from flask_restful import Resource, Api
from main import start

app = Flask(__name__)
api = Api(app)


@app.route('/tech/analysis/<ticker>', methods=["POST"])
def tech_analysis(ticker):
    body = start(ticker)
    return {'status': 'ok', 'data': body}


if __name__ == '__main__':
    app.run(debug=True)
