from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from FYP.entity.MedicalRecords import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 


@app.route('/StaffViewMedicalRecordController', methods=['GET', 'POST'])
def StaffViewMedicalRecordController():
    username = request.form['username']
    patientX, patientY = MedicalRecords.StaffViewMedicalRecord(username)
    session['patientY'] = patientY
    return render_template('StaffViewMedicalRecord.html', patientX = patientX)