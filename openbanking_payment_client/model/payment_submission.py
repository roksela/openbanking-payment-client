# coding: utf-8

"""
    Python client for Payment Initiation API

    Based on https://github.com/OpenBankingUK/payment-initiation-api-spec

    OpenAPI spec version: v1.1.1
    Spec: https://www.openbanking.org.uk/read-write-apis/
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from openbanking_payment_client.model.payment_setup_response_initiation import PaymentSetupResponseInitiation  # noqa: F401,E501


class PaymentSubmission(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'payment_id': 'str',
        'initiation': 'PaymentSetupResponseInitiation'
    }

    attribute_map = {
        'payment_id': 'PaymentId',
        'initiation': 'Initiation'
    }

    def __init__(self, payment_id=None, initiation=None):  # noqa: E501
        """PaymentSubmission - a model defined in Swagger"""  # noqa: E501

        self._payment_id = None
        self._initiation = None
        self.discriminator = None

        self.payment_id = payment_id
        self.initiation = initiation

    @property
    def payment_id(self):
        """Gets the payment_id of this PaymentSubmission.  # noqa: E501

        OB: Unique identification as assigned by the ASPSP to uniquely identify the payment setup resource.  # noqa: E501

        :return: The payment_id of this PaymentSubmission.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this PaymentSubmission.

        OB: Unique identification as assigned by the ASPSP to uniquely identify the payment setup resource.  # noqa: E501

        :param payment_id: The payment_id of this PaymentSubmission.  # noqa: E501
        :type: str
        """
        if payment_id is None:
            raise ValueError("Invalid value for `payment_id`, must not be `None`")  # noqa: E501
        if payment_id is not None and len(payment_id) > 128:
            raise ValueError("Invalid value for `payment_id`, length must be less than or equal to `128`")  # noqa: E501
        if payment_id is not None and len(payment_id) < 1:
            raise ValueError("Invalid value for `payment_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._payment_id = payment_id

    @property
    def initiation(self):
        """Gets the initiation of this PaymentSubmission.  # noqa: E501


        :return: The initiation of this PaymentSubmission.  # noqa: E501
        :rtype: PaymentSetupResponseInitiation
        """
        return self._initiation

    @initiation.setter
    def initiation(self, initiation):
        """Sets the initiation of this PaymentSubmission.


        :param initiation: The initiation of this PaymentSubmission.  # noqa: E501
        :type: PaymentSetupResponseInitiation
        """
        if initiation is None:
            raise ValueError("Invalid value for `initiation`, must not be `None`")  # noqa: E501

        self._initiation = initiation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PaymentSubmission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
