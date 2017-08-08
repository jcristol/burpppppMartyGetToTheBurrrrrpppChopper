#!/bin/python

import os
import json
from flask import Flask, render_template, redirect, url_for
import StringIO

app = Flask(__name__)
# The scraped Data yoooooo!!!!!!!!!!!!!!!!!!!!!!!!!!

@app.route('/mortydex/<morty>')
def morty_dex(morty):
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

    import code
    code.interct(local=locals())
    try:
        index = mortys.index(morty)
    except ValueError:
        print "Ooppps thats not a morty"
        return redirect(url_for('index'))
    big_image = imagePaths[index][1:]
    mortyInfo = infoJson[index]
    print "hello"
    print big_image
    import code
    code.interact(local=locals())
    return render_template('pokedex.html', image=big_image, info=mortyInfo)
    # return render_template('pokedex.html')

@app.route('/mortys')
def base():
    return redirect(url_for('morty_dex', morty='Ace_Pilot_Morty'))

@app.route('/')
def index():
    return "Hello your at the index"
    # return render_template('pokedex.html')
