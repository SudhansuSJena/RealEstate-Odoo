from odoo import fields, models


class RealEstateAmenities(models.Model):
    _name="real_estate.amenities"
    _description="Amenities for property"
    _inherit=["mail.thread"]

    
    amenity_name=fields.Char(string="Amenity Name", tracking=True)
    description=fields.Char(string="Description", tracking=True)