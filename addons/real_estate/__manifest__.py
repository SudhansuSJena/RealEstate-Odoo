{
  "name": "RealEstate Management",
  "author": "SUDHANSU SEKHAR JENA",
  "license": "LGPL-3",
  "version": "17.0.1.1",
  "sequence": "1",
  "depends": [
    "mail"  
  ],
  "data": [
      "security/ir.model.access.csv",
      "views/real_estate_sale_contracts_views.xml",
      "views/real_estate_bookings_views.xml",
      "views/real_estate_rent_contracts_views.xml",
      "views/real_estate_customers_views.xml",
      "views/real_estate_property_details_views.xml",
      "views/real_estate_connectivity_views.xml",
      "views/real_estate_features_views.xml",
      "views/real_estate_amenities.xml",
      "views/real_estate_property_types_views.xml",
      "views/real_estate_property_views.xml",
      "views/real_estate_menu.xml",
  ],
  "application": True, # Add this to make it appear in apps list
  "installable": True # Add this to make it installable
}
