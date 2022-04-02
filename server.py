import random
import string
from urllib import response
import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/sanity', methods=['GET'])
def check_sanity():
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response

@app.route('/question', methods=['POST'])
def question():
    question_contents = request.get_json()
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
    answer= jsonify({
        "answer": random_string
    })
    answer.status_code=200
    return answer

app.run(port=3000)