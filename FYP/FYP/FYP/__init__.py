"""
The flask application package.
"""

from flask import Flask
import pyrebase
import os
app = Flask(__name__)

#error here
from flask_mysqldb import MySQL
app.secret_key = 'facial_recognition'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'healthcare_db' #change into your own database
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1

mysql = MySQL(app)

#add firebase into as a new appplication with this config and change into strings dicts
firebaseConfig = {}

#init app
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()
 


import FYP.views
import FYP.controller.AdminSearchPatientController
import FYP.controller.AdminRegisterPatientController
import FYP.controller.AdminChangePatientCredentialsController
import FYP.controller.AdminChangePatientImageController
import FYP.controller.AdminAutomatedTrainingController
import FYP.controller.PatientViewAppointmentController
import FYP.controller.PatientCancelAppointmentController
import FYP.controller.PatientQueueNumberController
import FYP.controller.PatientUpdatePersonalDetailController
import FYP.controller.LoginController
import FYP.controller.FacialLoginController
import FYP.controller.FacialValidationController
import FYP.controller.LogoutController
import FYP.controller.PatientUpdatePersonalDetailController
import FYP.controller.StaffSearchPatientController
import FYP.controller.StaffViewPatientAppointmentController
import FYP.controller.StaffCreateAppointmentController
import FYP.controller.StaffViewMedicalRecordController
import FYP.controller.StaffCreateMedicalRecordController
import FYP.controller.StaffUpdateMedicalRecordController
import FYP.controller.StaffSearchDoctorController
import FYP.controller.StaffViewDoctorScheduleController
import FYP.controller.PatientBMIController
