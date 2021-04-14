# -*- coding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2019 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields, api, _


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def _check_make_stub_line(self, invoice):
        res = super(AccountPayment, self)._check_make_stub_line(invoice)
        res.update({'inv_num': invoice.name})
        return res
