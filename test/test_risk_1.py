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
from openbanking_payment_client.model.risk_1 import Risk1  # noqa: E501
from openbanking_payment_client.rest import ApiException


class TestRisk1(unittest.TestCase):
    """Risk1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRisk1(self):
        """Test Risk1"""
        # FIXME: construct object with mandatory attributes with example values
        # model = openbanking_payment_client.models.risk_1.Risk1()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()