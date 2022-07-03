from flask import Flask, request, jsonify

from preprocess import concatenate_question, preprocess
from t5base import T5BaseClass

debug_mode = False
initialized = False

app = Flask(__name__)

t5base = T5BaseClass()
initialized = True


@app.route('/get_status', methods=['GET'])
def get_status():
    return {'initialized': initialized}


@app.route('/answer', methods=['POST'])
def get_answer():
    request_data = request.json
    industries, faults, targets, currents, model = \
        request_data['industries'], request_data['faults'],\
        request_data['targets'], request_data['currents'], request_data['model']

    question = concatenate_question(industries, faults, targets, currents)
    question = preprocess(question)
    answers = t5base.answer(question)
    return jsonify(answers)


app.debug = False
app.run(host='0.0.0.0', port=5005)
