# This file is part account_asset_analytic_line_state module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool

def register():
    Pool.register(
        module='account_asset_analytic_line_state', type_='model')
    Pool.register(
        module='account_asset_analytic_line_state', type_='wizard')
    Pool.register(
        module='account_asset_analytic_line_state', type_='report')
