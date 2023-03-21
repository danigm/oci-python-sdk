# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .connection import Connection
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AmazonS3Connection(Connection):
    """
    Represents the metadata of a Amazon S3 Connection.
    """

    #: A constant which can be used with the technology_type property of a AmazonS3Connection.
    #: This constant has a value of "AMAZON_S3"
    TECHNOLOGY_TYPE_AMAZON_S3 = "AMAZON_S3"

    def __init__(self, **kwargs):
        """
        Initializes a new AmazonS3Connection object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.AmazonS3Connection.connection_type` attribute
        of this class is ``AMAZON_S3`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this AmazonS3Connection.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connection_type: str

        :param id:
            The value to assign to the id property of this AmazonS3Connection.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this AmazonS3Connection.
        :type display_name: str

        :param description:
            The value to assign to the description property of this AmazonS3Connection.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AmazonS3Connection.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AmazonS3Connection.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AmazonS3Connection.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this AmazonS3Connection.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AmazonS3Connection.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AmazonS3Connection.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this AmazonS3Connection.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AmazonS3Connection.
        :type time_updated: datetime

        :param vault_id:
            The value to assign to the vault_id property of this AmazonS3Connection.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this AmazonS3Connection.
        :type key_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this AmazonS3Connection.
        :type subnet_id: str

        :param ingress_ips:
            The value to assign to the ingress_ips property of this AmazonS3Connection.
        :type ingress_ips: list[oci.golden_gate.models.IngressIpDetails]

        :param nsg_ids:
            The value to assign to the nsg_ids property of this AmazonS3Connection.
        :type nsg_ids: list[str]

        :param technology_type:
            The value to assign to the technology_type property of this AmazonS3Connection.
            Allowed values for this property are: "AMAZON_S3", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type technology_type: str

        :param access_key_id:
            The value to assign to the access_key_id property of this AmazonS3Connection.
        :type access_key_id: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'vault_id': 'str',
            'key_id': 'str',
            'subnet_id': 'str',
            'ingress_ips': 'list[IngressIpDetails]',
            'nsg_ids': 'list[str]',
            'technology_type': 'str',
            'access_key_id': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'subnet_id': 'subnetId',
            'ingress_ips': 'ingressIps',
            'nsg_ids': 'nsgIds',
            'technology_type': 'technologyType',
            'access_key_id': 'accessKeyId'
        }

        self._connection_type = None
        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._vault_id = None
        self._key_id = None
        self._subnet_id = None
        self._ingress_ips = None
        self._nsg_ids = None
        self._technology_type = None
        self._access_key_id = None
        self._connection_type = 'AMAZON_S3'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this AmazonS3Connection.
        The Amazon S3 technology type.

        Allowed values for this property are: "AMAZON_S3", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The technology_type of this AmazonS3Connection.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this AmazonS3Connection.
        The Amazon S3 technology type.


        :param technology_type: The technology_type of this AmazonS3Connection.
        :type: str
        """
        allowed_values = ["AMAZON_S3"]
        if not value_allowed_none_or_none_sentinel(technology_type, allowed_values):
            technology_type = 'UNKNOWN_ENUM_VALUE'
        self._technology_type = technology_type

    @property
    def access_key_id(self):
        """
        **[Required]** Gets the access_key_id of this AmazonS3Connection.
        Access key ID to access the Amazon S3 bucket.
        e.g.: \"this-is-not-the-secret\"


        :return: The access_key_id of this AmazonS3Connection.
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """
        Sets the access_key_id of this AmazonS3Connection.
        Access key ID to access the Amazon S3 bucket.
        e.g.: \"this-is-not-the-secret\"


        :param access_key_id: The access_key_id of this AmazonS3Connection.
        :type: str
        """
        self._access_key_id = access_key_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
