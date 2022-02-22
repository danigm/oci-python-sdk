# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_read_attribute import AbstractReadAttribute
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OracleReadAttributes(AbstractReadAttribute):
    """
    Properties to configure reading from an Oracle Database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OracleReadAttributes object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.OracleReadAttributes.model_type` attribute
        of this class is ``ORACLE_READ_ATTRIBUTE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this OracleReadAttributes.
            Allowed values for this property are: "ORACLEREADATTRIBUTE", "ORACLE_READ_ATTRIBUTE", "BICC_READ_ATTRIBUTE"
        :type model_type: str

        :param fetch_size:
            The value to assign to the fetch_size property of this OracleReadAttributes.
        :type fetch_size: int

        """
        self.swagger_types = {
            'model_type': 'str',
            'fetch_size': 'int'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'fetch_size': 'fetchSize'
        }

        self._model_type = None
        self._fetch_size = None
        self._model_type = 'ORACLE_READ_ATTRIBUTE'

    @property
    def fetch_size(self):
        """
        Gets the fetch_size of this OracleReadAttributes.
        The fetch size for reading.


        :return: The fetch_size of this OracleReadAttributes.
        :rtype: int
        """
        return self._fetch_size

    @fetch_size.setter
    def fetch_size(self, fetch_size):
        """
        Sets the fetch_size of this OracleReadAttributes.
        The fetch size for reading.


        :param fetch_size: The fetch_size of this OracleReadAttributes.
        :type: int
        """
        self._fetch_size = fetch_size

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
