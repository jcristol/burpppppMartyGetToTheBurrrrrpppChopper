#!/bin/python

import os
import json
from flask import Flask, render_template, redirect, url_for
import StringIO
import random

app = Flask(__name__)

mortyIndex = 0

# The scraped Data yoooooo!!!!!!!!!!!!!!!!!!!!!!!!!!
mortyDataPaths = []
mortys = []
for filename in os.listdir('./static/data'):
    if filename.endswith("Morty"):
        mortyDataPaths.append("./static/data/" + filename)
        mortys.append(filename)
imagePaths = [(path + "/big_image.png") for path in mortyDataPaths]
iconPaths = [(path + "/icon.png") for path in mortyDataPaths]
infoPaths = [(path + "/info.json") for path in mortyDataPaths]
infoJsonFiles = [open(path, 'r') for path in infoPaths]
infoJson = [json.loads(f.read()) for f in infoJsonFiles]

#sounds i "scraped"
soundPaths = []
for filename in os.listdir('./static/sounds'):
    if filename.endswith(".wav"):
        soundPaths.append("./static/sounds/" + filename)

@app.route('/right')
def right_morty():
    global mortyIndex
    mortyIndex = (mortyIndex + 1) % (len(mortys))
    print "len %i" % len(mortys)
    print "index %i" % mortyIndex
    return redirect(url_for('display_morty', morty=mortys[mortyIndex]))

@app.route('/left')
def left_morty():
    global mortyIndex
    mortyIndex = mortyIndex - 1
    if mortyIndex < 0:
        mortyIndex = len(mortys) - 1
    print "len %i" % len(mortys)
    print "index %i" % mortyIndex
    return redirect(url_for('display_morty', morty=mortys[mortyIndex]))

@app.route('/mortydex/<morty>')
def display_morty(morty):
    randomSound = random.choice(soundPaths)[1:]
    try:
        index = mortys.index(morty)
    except ValueError:
        print "Ooppps thats not a morty"
        return redirect(url_for('index'))
    big_image = imagePaths[index][1:]
    mortyInfo = infoJson[index]
    return render_template('pokedex.html', image=big_image, info=mortyInfo, noise=randomSound)

@app.route('/')
def index():
    return "Hello you're at the index"
