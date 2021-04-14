# -*- coding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2019 (http://www.bistasolutions.com)
#
##############################################################################
{
    'name': 'US Check Printing',
    'author': 'Bista solutions',
    'category': 'Account',
    'summary': 'Check printing',
    'website': 'http://www.Bistasolutions.com',
    'description': """
        """,
    'version': '13.0',
    'depends': ['l10n_us_check_printing', 'account_accountant'],
    'data': [
        'report/print_check.xml'
    ],
    'installable': True,
    'auto_install': False,
}
