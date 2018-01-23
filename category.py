# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.pyson import Eval
from trytond.modules.product_esale.tools import slugify

__all__ = ['Category']


class Category:
    __metaclass__ = PoolMeta
    __name__ = "product.category"
    esale_active = fields.Boolean('Active eSale')
    default_sort_by = fields.Selection([
            ('', ''),
            ('position', 'Position'),
            ('name', 'Name'),
            ('price', 'Price'),
            ('date', 'Date'),
            ], 'Default Product Listing Sort (Sort By)',
        states={
            'invisible': ~Eval('esale_active', True),
        }, depends=['esale_active'])
    slug = fields.Char('Slug', size=None, translate=True,
        states={
            'invisible': ~Eval('esale_active', True),
            'required': Eval('esale_active', True),
        }, depends=['esale_active'])
    full_slug = fields.Function(fields.Char('Full Slug',
        states={
            'invisible': ~Eval('esale_active', True),
        }, depends=['esale_active']), 'get_full_slug')
    description = fields.Text('Description', translate=True,
        states={
            'invisible': ~Eval('esale_active', True),
        }, depends=['esale_active'])
    metadescription = fields.Char('MetaDescription', size=155, translate=True,
        states={
            'invisible': ~Eval('esale_active', True),
        }, depends=['esale_active'])
    metakeyword = fields.Char('MetaKeyword', size=155, translate=True,
        states={
            'invisible': ~Eval('esale_active', True),
        }, depends=['esale_active'])
    metatitle = fields.Char('MetaTitle', size=155, translate=True,
        states={
            'invisible': ~Eval('esale_active', True),
        }, depends=['esale_active'])
    include_in_menu = fields.Boolean('Included in Menu',
        states={
            'invisible': ~Eval('esale_active', True),
        }, depends=['esale_active'])

    @staticmethod
    def default_default_sort_by():
        return 'position'

    @staticmethod
    def default_include_in_menu():
        return True

    @fields.depends('name', 'slug')
    def on_change_name(self):
        if hasattr(self, 'on_change_name'):
            super(Category, self).on_change_name()

        if self.name and not self.slug:
            self.slug = slugify(self.name)

    def get_full_slug(self, name):
        if self.esale_active and self.parent:
            parent_slug = self.parent.get_full_slug(name)
            if parent_slug and self.slug:
                return self.parent.get_full_slug(name) + '/' + self.slug
        return self.slug

    @classmethod
    def view_attributes(cls):
        esale_attribute = [
            ('//page[@id="esale-general"]', 'states', {
                    'invisible': ~Eval('esale_active'),
                    }),
            ('//page[@id="esale-seo"]', 'states', {
                    'invisible': ~Eval('esale_active'),
                    }),
            ]
        if hasattr(cls, 'view_attributes'):
            return super(Category, cls).view_attributes() + esale_attribute
        return esale_attribute
