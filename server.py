import random
import string
from urllib import response
import flask
from flask import jsonify, request
from eva.nlp import NLP
from eva.oracle import Oracle
from eva.wiki_search import generate_wiki_page

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
    generate_wiki_page(question_contents["question_text"])
    with open('paragraph.txt', 'r', encoding="utf-8") as f:
        paragraph = f.read()
    oracle = Oracle(question_contents, paragraph)
    answer= jsonify({
        "answer": oracle.answer()
    })
    answer.status_code=200
    return answer

app.run(port=3000)
