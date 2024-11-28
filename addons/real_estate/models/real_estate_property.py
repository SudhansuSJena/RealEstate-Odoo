from odoo import models, exceptions, fields


class RealEstateProperty(models.Model):
    _name="real_estate.property"
    _description="REAL ESTATE PROPERTY MASTER"
    _inherit=["mail.thread"]

    name=fields.Char(string="Property Name", tracking=True)
    typeOfProperty=fields.Many2one(
        comodel_name="real_estate.property_types",
        string="Type of Property",
        on_delete='cascade',
        domain=[],
        required=True,
        help='Select the type of property',
        tracking=True
    )
    status=fields.Selection([
        ('available', 'Available'),
        ('on sale', 'On Sale'), 
        ('on lease', 'On Lease'), 
        ('sold', 'Sold')
    ], tracking=True)
    area=fields.Float(string="Property Area", tracking=True)
    geo_location=fields.Char(string="Geo-Location", tracking=True)

    