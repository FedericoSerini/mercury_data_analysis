from flask import Flask
from main import start

app = Flask(__name__)


@app.route('/tech/analysis/ALL', methods=["POST"])
def tech_analysis():
    body = start()
    return {'status': 'ok', 'data': body}


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
