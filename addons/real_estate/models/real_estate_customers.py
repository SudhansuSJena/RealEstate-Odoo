from odoo import models, fields


class RealEstateCustomers(models.Model):
    _name="real_estate.customers"
    _description="Customers to buy property"
    _inherit=['mail.thread']

    customer_name = fields.Char(string="Customer's Name")
    customer_phone_number = fields.Integer(string="Customer's Phone-Number")
    customer_email = fields.Char(string="Customer's email")
    booking_ids = fields.One2many(
        comodel_name="real_estate.bookings",
        inverse_name="customer_id",
        string="Your Bookings",
        domain=[],
        required=True,
        tracking=True
    )
    rental_contract_ids = fields.One2many(
        comodel_name="real_estate.rent_contracts",
        inverse_name="tenant_id",
        domain=[],
        required=True,
        tracking=True
    )

    sale_contract_ids = fields.One2many(
        comodel_name="real_estate.sale_contracts",
        inverse_name="buyer_id",
        string="Sale Contracts",
        domain=[],
        required=True,
        help="Customer's Sale Contracts"
    )