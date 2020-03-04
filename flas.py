# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:54:55 2020

@author: mamed
"""

from flask import Flask,render_template

app=Flask(__name__)
@app.route("/")
def index():
    return "Ana sayfa"
if __name__=="__main__":
    app.run()