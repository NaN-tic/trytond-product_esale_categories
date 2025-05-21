# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.pyson import Eval
from trytond.modules.voyager import slugify


class Category(metaclass=PoolMeta):
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
        })
    slug = fields.Char('Slug', size=None, translate=True,
        states={
            'invisible': ~Eval('esale_active', True),
            'required': Eval('esale_active', True),
        })
    full_slug = fields.Function(fields.Char('Full Slug',
        states={
            'invisible': ~Eval('esale_active', True),
        }), 'get_full_slug')
    description = fields.Text('Description', translate=True,
        states={
            'invisible': ~Eval('esale_active', True),
        })
    metadescription = fields.Char('MetaDescription', size=155, translate=True,
        states={
            'invisible': ~Eval('esale_active', True),
        })
    metakeyword = fields.Char('MetaKeyword', size=155, translate=True,
        states={
            'invisible': ~Eval('esale_active', True),
        })
    metatitle = fields.Char('MetaTitle', size=155, translate=True,
        states={
            'invisible': ~Eval('esale_active', True),
        })
    include_in_menu = fields.Boolean('Included in Menu',
        states={
            'invisible': ~Eval('esale_active', True),
        })

    @staticmethod
    def default_default_sort_by():
        return 'position'

    @staticmethod
    def default_include_in_menu():
        return True

    @fields.depends('name', 'slug')
    def on_change_name(self):
        try:
            super(Category, self).on_change_name()
        except:
            pass

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
