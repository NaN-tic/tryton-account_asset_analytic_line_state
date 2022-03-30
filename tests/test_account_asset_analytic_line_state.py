# This file is part account_asset_analytic_line_state module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class AccountAssetAnalyticLineStateTestCase(ModuleTestCase):
    'Test Account Asset Analytic Line State module'
    module = 'account_asset_analytic_line_state'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            AccountAssetAnalyticLineStateTestCase))
    return suite
