from odoo import models, fields


class RealEstateCustomers(models.Model):
    _name="real_estate.customers"
    _description="Customers to buy property"
    _inherit=['mail.thread']

    name = fields.Char(string="Customer's Name", tracking=True)
    image = fields.Image(string="Customer's Image")
    phone_number = fields.Char(string="Customer's Phone-Number", tracking=True)
    email = fields.Char(string="Customer's email", tracking=True)
    booking_ids = fields.One2many(
        comodel_name="real_estate.bookings",
        inverse_name="customer_id",
        string="Your Bookings",
        domain=[],
        tracking=True
    )

    rental_contract_ids = fields.One2many(
        comodel_name="real_estate.rent_contracts",
        inverse_name="tenant_id",
        string="Your Rental Contracts",
        domain=[],
        tracking=True,
    )

    sale_contract_ids = fields.One2many(
        comodel_name="real_estate.sale_contracts",
        inverse_name="buyer_id",
        string="Sale Contracts",
        domain=[],
        help="Customer's Sale Contracts",
        tracking=True,
    )