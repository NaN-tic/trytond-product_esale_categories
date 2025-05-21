
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.modules.company.tests import CompanyTestMixin
from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.pool import Pool


class ProductEsaleCategoriesTestCase(CompanyTestMixin, ModuleTestCase):
    'Test ProductEsaleCategories module'
    module = 'product_esale_categories'

    @with_transaction()
    def test_slugify(self):
        'Test slugify'
        pool = Pool()
        Category = pool.get('product.category')

        category = Category()
        category.name = 'Menu Demo'
        category.slug = None
        category.on_change_name()
        self.assertEqual(category.slug, 'menu-demo')

del ModuleTestCase
