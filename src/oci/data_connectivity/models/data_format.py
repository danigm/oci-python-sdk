# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataFormat(object):
    """
    The data format object.
    """

    #: A constant which can be used with the type property of a DataFormat.
    #: This constant has a value of "JSON"
    TYPE_JSON = "JSON"

    #: A constant which can be used with the type property of a DataFormat.
    #: This constant has a value of "CSV"
    TYPE_CSV = "CSV"

    #: A constant which can be used with the type property of a DataFormat.
    #: This constant has a value of "PARQUET"
    TYPE_PARQUET = "PARQUET"

    #: A constant which can be used with the type property of a DataFormat.
    #: This constant has a value of "AVRO"
    TYPE_AVRO = "AVRO"

    def __init__(self, **kwargs):
        """
        Initializes a new DataFormat object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param format_attribute:
            The value to assign to the format_attribute property of this DataFormat.
        :type format_attribute: oci.data_connectivity.models.AbstractFormatAttribute

        :param type:
            The value to assign to the type property of this DataFormat.
            Allowed values for this property are: "JSON", "CSV", "PARQUET", "AVRO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param compression_config:
            The value to assign to the compression_config property of this DataFormat.
        :type compression_config: oci.data_connectivity.models.Compression

        """
        self.swagger_types = {
            'format_attribute': 'AbstractFormatAttribute',
            'type': 'str',
            'compression_config': 'Compression'
        }

        self.attribute_map = {
            'format_attribute': 'formatAttribute',
            'type': 'type',
            'compression_config': 'compressionConfig'
        }

        self._format_attribute = None
        self._type = None
        self._compression_config = None

    @property
    def format_attribute(self):
        """
        Gets the format_attribute of this DataFormat.

        :return: The format_attribute of this DataFormat.
        :rtype: oci.data_connectivity.models.AbstractFormatAttribute
        """
        return self._format_attribute

    @format_attribute.setter
    def format_attribute(self, format_attribute):
        """
        Sets the format_attribute of this DataFormat.

        :param format_attribute: The format_attribute of this DataFormat.
        :type: oci.data_connectivity.models.AbstractFormatAttribute
        """
        self._format_attribute = format_attribute

    @property
    def type(self):
        """
        **[Required]** Gets the type of this DataFormat.
        type

        Allowed values for this property are: "JSON", "CSV", "PARQUET", "AVRO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this DataFormat.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DataFormat.
        type


        :param type: The type of this DataFormat.
        :type: str
        """
        allowed_values = ["JSON", "CSV", "PARQUET", "AVRO"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def compression_config(self):
        """
        Gets the compression_config of this DataFormat.

        :return: The compression_config of this DataFormat.
        :rtype: oci.data_connectivity.models.Compression
        """
        return self._compression_config

    @compression_config.setter
    def compression_config(self, compression_config):
        """
        Sets the compression_config of this DataFormat.

        :param compression_config: The compression_config of this DataFormat.
        :type: oci.data_connectivity.models.Compression
        """
        self._compression_config = compression_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
