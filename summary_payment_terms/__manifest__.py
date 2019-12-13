# -*- coding: utf-8 -*-
{
    'name': "summary_payment_terms",

    'summary': """
        Summary by Payment Terms
        """,

    'description': """
        Informe de facturas por formas de cobro. Este informe muestra las facturas cobradas por Cheque/Efectivo y saca los totales. Antes de hacerlo hay que seleccionar las facturas.
    """,

    'author': "GSol Soluciones Informáticas",
    'website': "http://www.gsol.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/reports.xml',
        'report/summary_payment_terms.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}