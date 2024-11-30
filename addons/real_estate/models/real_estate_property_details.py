from odoo import models, fields


class RealEstatePropertyDetails(models.Model):
    _name = "real_estate.property_details"
    _description="Details of RealEstate Property"
    _inherit=["mail.thread"]


    property_id = fields.Many2one(
        comodel_name="real_estate.property",
        string="Property Details",
        ondelete="set null",
        required=True,
        help='Property details of selected Property'
    )
    bedroom_area = fields.Float(string="Bedroom area")
    bathroom_area = fields.Float(string="Bathroom area")
    kitchen_area = fields.Float(string="Kitchen area")
    hall_area = fields.Float(string="Hall area")
    parking_area = fields.Float(string="Parking area")
    backyard_area = fields.Float(string="Backyard area")
    total_bedrooms = fields.Integer(string="Total bedrooms")
    total_bathrooms = fields.Integer(string="Total bathrooms")
    total_floors = fields.Integer(string="Total floors")
    