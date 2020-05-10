from __future__ import print_function

from flask import Flask, render_template,request, make_response
import os
app = Flask(__name__)
from keras.callbacks import LambdaCallback
from keras.models import Model, load_model, Sequential
from keras.layers import Dense, Activation, Dropout, Input, Masking
from keras.layers import LSTM
from keras.utils.data_utils import get_file
from keras.preprocessing.sequence import pad_sequences
import shakes
import sys


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/get_data', methods=['GET'])
def getLink():
    # print("hello")
    input = request.args.get('begin_with')
    length = request.args.get('length')
    print(input)
    print("hello")

    
    # predictedFlair = predictFlairByLink(postLink)

    
    return


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 8080)))
