from . import odoo_xmlrcp_migration


def map_product_type(self, value, field, plan, row, field_collection='fields'):

    if value != 'service':
        return 'consu'
    return value


setattr(odoo_xmlrcp_migration, 'map_product_type', map_product_type)
