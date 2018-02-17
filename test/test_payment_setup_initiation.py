# coding: utf-8

"""
    Python client for Payment Initiation API

    Based on https://github.com/OpenBankingUK/payment-initiation-api-spec

    OpenAPI spec version: v1.1.1
    Spec: https://www.openbanking.org.uk/read-write-apis/
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import openbanking_payment_client
from openbanking_payment_client.model.payment_setup_initiation import PaymentSetupInitiation  # noqa: E501
from openbanking_payment_client.rest import ApiException


class TestPaymentSetupInitiation(unittest.TestCase):
    """PaymentSetupInitiation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentSetupInitiation(self):
        """Test PaymentSetupInitiation"""
        # FIXME: construct object with mandatory attributes with example values
        # model = openbanking_payment_client.models.payment_setup_initiation.PaymentSetupInitiation()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
