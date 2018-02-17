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

from openbanking_payment_client.model.payment_setup_post_response_links import PaymentSetupPOSTResponseLinks  # noqa: F401,E501
from openbanking_payment_client.model.payment_setup_post_response_meta import PaymentSetupPOSTResponseMeta  # noqa: F401,E501
from openbanking_payment_client.model.payment_setup_response import PaymentSetupResponse  # noqa: F401,E501
from openbanking_payment_client.model.risk1 import Risk1  # noqa: F401,E501


class PaymentSetupPOSTResponse(object):
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
        'data': 'PaymentSetupResponse',
        'risk': 'Risk1',
        'links': 'PaymentSetupPOSTResponseLinks',
        'meta': 'PaymentSetupPOSTResponseMeta'
    }

    attribute_map = {
        'data': 'Data',
        'risk': 'Risk',
        'links': 'Links',
        'meta': 'Meta'
    }

    def __init__(self, data=None, risk=None, links=None, meta=None):  # noqa: E501
        """PaymentSetupPOSTResponse - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._risk = None
        self._links = None
        self._meta = None
        self.discriminator = None

        self.data = data
        self.risk = risk
        self.links = links
        self.meta = meta

    @property
    def data(self):
        """Gets the data of this PaymentSetupPOSTResponse.  # noqa: E501


        :return: The data of this PaymentSetupPOSTResponse.  # noqa: E501
        :rtype: PaymentSetupResponse
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PaymentSetupPOSTResponse.


        :param data: The data of this PaymentSetupPOSTResponse.  # noqa: E501
        :type: PaymentSetupResponse
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def risk(self):
        """Gets the risk of this PaymentSetupPOSTResponse.  # noqa: E501


        :return: The risk of this PaymentSetupPOSTResponse.  # noqa: E501
        :rtype: Risk1
        """
        return self._risk

    @risk.setter
    def risk(self, risk):
        """Sets the risk of this PaymentSetupPOSTResponse.


        :param risk: The risk of this PaymentSetupPOSTResponse.  # noqa: E501
        :type: Risk1
        """
        if risk is None:
            raise ValueError("Invalid value for `risk`, must not be `None`")  # noqa: E501

        self._risk = risk

    @property
    def links(self):
        """Gets the links of this PaymentSetupPOSTResponse.  # noqa: E501


        :return: The links of this PaymentSetupPOSTResponse.  # noqa: E501
        :rtype: PaymentSetupPOSTResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PaymentSetupPOSTResponse.


        :param links: The links of this PaymentSetupPOSTResponse.  # noqa: E501
        :type: PaymentSetupPOSTResponseLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def meta(self):
        """Gets the meta of this PaymentSetupPOSTResponse.  # noqa: E501


        :return: The meta of this PaymentSetupPOSTResponse.  # noqa: E501
        :rtype: PaymentSetupPOSTResponseMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this PaymentSetupPOSTResponse.


        :param meta: The meta of this PaymentSetupPOSTResponse.  # noqa: E501
        :type: PaymentSetupPOSTResponseMeta
        """
        if meta is None:
            raise ValueError("Invalid value for `meta`, must not be `None`")  # noqa: E501

        self._meta = meta

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
        if not isinstance(other, PaymentSetupPOSTResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other