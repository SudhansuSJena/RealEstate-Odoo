from odoo import models, exceptions, fields


class RealEstateProperty(models.Model):
    _name = "real_estate.property"
    _description = "REAL ESTATE PROPERTY MASTER"
    _inherit = ["mail.thread"]

    name = fields.Char(string="Property Name", tracking=True)
    typeOfProperty = fields.Many2one(
        comodel_name = "real_estate.property_types",
        string="Type of Property",
        on_delete='cascade',
        domain=[],
        required=True,
        help='Select the type of property',
        tracking=True
    )
    status=fields.Selection([
        ('available', 'Available'),
        ('booked', 'Booked'), 
        ('sold', 'Sold'), 
        ('leased', 'Leased')
    ], string="Property Status", tracking=True)

    area=fields.Float(string="Property Area", tracking=True)
    geo_location=fields.Char(string="Geo-Location", tracking=True)
    amenity = fields.Many2many(
        comodel_name = 'real_estate.amenities',
        relation = 'property_amenities_rel',
        column1 = 'property_id',
        column2 = 'amenities_id',
        string = 'Property Amenities',
        domain = [],
        help = 'Select Amenities for Property'
    )

    feature = fields.Many2many(
        comodel_name = 'real_estate.features',
        relation = 'property_features_rel',
        column1 = 'property_id',
        column2 = 'features_id',
        string = 'Property Features',
        domain = [],
        help = 'Select Features for Property'
    )

    connectivity = fields.Many2many(
        comodel_name = 'real_estate.connectivity',
        relation = 'property_connectivity_rel',
        column1 = 'property_id',
        column2 = 'connectivity_id',
        string = 'Property Connectivity',
        domain = [],
        help = 'See the connectivities from the property.'
    )

    
    

    