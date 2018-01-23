# This file is part product_esale_categories module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import category


def register():
    Pool.register(
        category.Category,
        module='product_esale_categories', type_='model')
