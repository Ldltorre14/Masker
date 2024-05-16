from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)


@app.route('/<name>')
def printName(name):
    return "Hi, {}".format(name)

@app.route('/')
def index():
    return "Hello World"

