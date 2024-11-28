from odoo import models, fields


class RealEstateFeatures(models.Model):
    _name="real_estate.features"
    _description="Real Estate Features"
    _inherit=["mail.thread"]


    feature_name=fields.Char(string="Feature Name")
    description=fields.Char(string="Description")