# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 12:54:33 2020

@author: Mammad Abbasli
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

@app.route("/<string:model>/<string:extcolor>/<string:years>",methods=['GET'])
def find(model,extcolor,years):
     
     cursor = mysql.connection.cursor()
     sorgu ="Select *From car_info where models like '%"+ model +"%' and ext_color like '%"+ extcolor +"%'and year like '%"+ years +"%' "
     cursor.execute(sorgu)
     mysql.connection.commit()
     data=cursor.fetchall()
     cursor.close()
 
     return jsonify(data)

if __name__=="__main__":

    app.run()
