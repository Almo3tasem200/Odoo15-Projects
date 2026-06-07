from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient" #hospital_patient table in db
    _description = "Hospital Patient"

    name = fields.Char(string="Patient Name")
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ("male", "Male"),
        ("female", "Female")
    ],string="Gender")
