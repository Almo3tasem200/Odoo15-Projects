from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient" #hospital_patient table in db
    _description = "Hospital Patient"
    