from flask import Flask, render_template, jsonify
import json
import random
import os

app = Flask(__name__)

with open('pokeneas.json', 'r') as file:
    pokeneas = json.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokeneaRandom', methods=['GET'])
def obtain():
    pokenea = random.choice(pokeneas)
    pokenea['container_id'] = os.uname()[1]
    return jsonify(pokenea)

@app.route('/pokeneaView')
def pokeneaView():
    return render_template('pokeneaView.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
