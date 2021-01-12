# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PropertyOverride(object):
    """
    Property overrides at the scope of objects.
    For example, if you want to use logSourceName as 'xyz' for all objects that conatins string 'abc/' then
    define matchType as 'contains', matchValue as 'abc/', propertyName as 'logSourceName' and propertyValue as 'xyz'.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PropertyOverride object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param match_type:
            The value to assign to the match_type property of this PropertyOverride.
        :type match_type: str

        :param match_value:
            The value to assign to the match_value property of this PropertyOverride.
        :type match_value: str

        :param property_name:
            The value to assign to the property_name property of this PropertyOverride.
        :type property_name: str

        :param property_value:
            The value to assign to the property_value property of this PropertyOverride.
        :type property_value: str

        """
        self.swagger_types = {
            'match_type': 'str',
            'match_value': 'str',
            'property_name': 'str',
            'property_value': 'str'
        }

        self.attribute_map = {
            'match_type': 'matchType',
            'match_value': 'matchValue',
            'property_name': 'propertyName',
            'property_value': 'propertyValue'
        }

        self._match_type = None
        self._match_value = None
        self._property_name = None
        self._property_value = None

    @property
    def match_type(self):
        """
        Gets the match_type of this PropertyOverride.
        Match Type. Accepted values are: contains


        :return: The match_type of this PropertyOverride.
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """
        Sets the match_type of this PropertyOverride.
        Match Type. Accepted values are: contains


        :param match_type: The match_type of this PropertyOverride.
        :type: str
        """
        self._match_type = match_type

    @property
    def match_value(self):
        """
        Gets the match_value of this PropertyOverride.
        Match Value.


        :return: The match_value of this PropertyOverride.
        :rtype: str
        """
        return self._match_value

    @match_value.setter
    def match_value(self, match_value):
        """
        Sets the match_value of this PropertyOverride.
        Match Value.


        :param match_value: The match_value of this PropertyOverride.
        :type: str
        """
        self._match_value = match_value

    @property
    def property_name(self):
        """
        Gets the property_name of this PropertyOverride.
        Property to override. Accepted values are: logSourceName, charEncoding.


        :return: The property_name of this PropertyOverride.
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """
        Sets the property_name of this PropertyOverride.
        Property to override. Accepted values are: logSourceName, charEncoding.


        :param property_name: The property_name of this PropertyOverride.
        :type: str
        """
        self._property_name = property_name

    @property
    def property_value(self):
        """
        Gets the property_value of this PropertyOverride.
        Value.


        :return: The property_value of this PropertyOverride.
        :rtype: str
        """
        return self._property_value

    @property_value.setter
    def property_value(self, property_value):
        """
        Sets the property_value of this PropertyOverride.
        Value.


        :param property_value: The property_value of this PropertyOverride.
        :type: str
        """
        self._property_value = property_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
