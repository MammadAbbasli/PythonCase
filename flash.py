# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 12:54:33 2020

@author: mamed
"""

from flask import Flask,jsonify
from flask_mysqldb import MySQL



app=Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "case"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)
@app.route("/list/<extColor>/<model>/<year>",methods=['GET'])

def liste(extColor,model,year):
    print(extColor,model,year)
    cursor = mysql.connection.cursor()
    sorgu = ("Select * From car_info wehere ext_color='{0}'and models='{1}'and year='{2}'".format(extColor,model,year))
    cursor.execute(sorgu)
    data=cursor.fetchall()
    cursor.close()
    return jsonify(data)

if __name__=="__main__":
#    app.debug = True
    use_reloader=False
    app.run()

