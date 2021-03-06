# coding: utf-8

"""
    Open Legal Data API

    With the Open Legal Data API you can access various data from the legal domain, e.g. law text or case files. The data may be used for semantic analysis or to create statistics. For more information visit our website.  # noqa: E501

    OpenAPI spec version: v1
    Contact: api@openlegaldata.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class State(object):
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
        'id': 'int',
        'name': 'str',
        'country': 'int',
        'slug': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'country': 'country',
        'slug': 'slug'
    }

    def __init__(self, id=None, name=None, country=None, slug=None):  # noqa: E501
        """State - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._country = None
        self._slug = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.country = country
        self.slug = slug

    @property
    def id(self):
        """Gets the id of this State.  # noqa: E501


        :return: The id of this State.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this State.


        :param id: The id of this State.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this State.  # noqa: E501


        :return: The name of this State.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this State.


        :param name: The name of this State.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501

        self._name = name

    @property
    def country(self):
        """Gets the country of this State.  # noqa: E501


        :return: The country of this State.  # noqa: E501
        :rtype: int
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this State.


        :param country: The country of this State.  # noqa: E501
        :type: int
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def slug(self):
        """Gets the slug of this State.  # noqa: E501

        Name field as slug  # noqa: E501

        :return: The slug of this State.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this State.

        Name field as slug  # noqa: E501

        :param slug: The slug of this State.  # noqa: E501
        :type: str
        """
        if slug is None:
            raise ValueError("Invalid value for `slug`, must not be `None`")  # noqa: E501
        if slug is not None and len(slug) > 50:
            raise ValueError("Invalid value for `slug`, length must be less than or equal to `50`")  # noqa: E501
        if slug is not None and not re.search('^[-a-zA-Z0-9_]+$', slug):  # noqa: E501
            raise ValueError("Invalid value for `slug`, must be a follow pattern or equal to `/^[-a-zA-Z0-9_]+$/`")  # noqa: E501

        self._slug = slug

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
        if not isinstance(other, State):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
