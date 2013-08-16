import os
from flask import Flask, request
from subprocess import call
from simple_rec import run_rec
app = Flask(__name__)

@app.route('/rec',methods=['POST'])
def rec():
    file=request.files['file']
    file.save('search.png')
    return str(run_rec())

if __name__ == "__main__":
    app.run(host='0.0.0.0')
