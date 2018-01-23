# This file is part product_esale_categories module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class ProductEsaleCategoriesTestCase(ModuleTestCase):
    'Test Product Esale Categories module'
    module = 'product_esale_categories'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            ProductEsaleCategoriesTestCase))
    return suite
