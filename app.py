from flask import Flask, render_template, jsonify
import json
import random
import os

app = Flask(__name__)

with open('pokeneas.json', 'r') as file:
    pokeneas = json.load(file)

def get_pokenea():
    return random.choice(pokeneas)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokeneaRandom', methods=['GET'])
def obtain():
    pokenea = get_pokenea()
    pokenea['container_id'] = os.uname()[1]
    return jsonify(pokenea)

@app.route('/pokeneaView')
def pokeneaView():
    pokenea = get_pokenea()
    container_id = os.uname()[1]
    return render_template('pokeneaView.html', pokenea = pokenea, container_id=container_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
