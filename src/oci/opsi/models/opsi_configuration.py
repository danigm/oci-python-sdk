# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OpsiConfiguration(object):
    """
    OPSI configuration.
    """

    #: A constant which can be used with the opsi_config_type property of a OpsiConfiguration.
    #: This constant has a value of "UX_CONFIGURATION"
    OPSI_CONFIG_TYPE_UX_CONFIGURATION = "UX_CONFIGURATION"

    #: A constant which can be used with the lifecycle_state property of a OpsiConfiguration.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OpsiConfiguration.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a OpsiConfiguration.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OpsiConfiguration.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a OpsiConfiguration.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a OpsiConfiguration.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new OpsiConfiguration object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.OpsiUxConfiguration`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OpsiConfiguration.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OpsiConfiguration.
        :type compartment_id: str

        :param opsi_config_type:
            The value to assign to the opsi_config_type property of this OpsiConfiguration.
            Allowed values for this property are: "UX_CONFIGURATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type opsi_config_type: str

        :param display_name:
            The value to assign to the display_name property of this OpsiConfiguration.
        :type display_name: str

        :param description:
            The value to assign to the description property of this OpsiConfiguration.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OpsiConfiguration.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OpsiConfiguration.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OpsiConfiguration.
        :type system_tags: dict(str, dict(str, object))

        :param time_created:
            The value to assign to the time_created property of this OpsiConfiguration.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OpsiConfiguration.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OpsiConfiguration.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OpsiConfiguration.
        :type lifecycle_details: str

        :param config_items:
            The value to assign to the config_items property of this OpsiConfiguration.
        :type config_items: list[oci.opsi.models.OpsiConfigurationConfigurationItemSummary]

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'opsi_config_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'config_items': 'list[OpsiConfigurationConfigurationItemSummary]'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'opsi_config_type': 'opsiConfigType',
            'display_name': 'displayName',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'config_items': 'configItems'
        }

        self._id = None
        self._compartment_id = None
        self._opsi_config_type = None
        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._config_items = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['opsiConfigType']

        if type == 'UX_CONFIGURATION':
            return 'OpsiUxConfiguration'
        else:
            return 'OpsiConfiguration'

    @property
    def id(self):
        """
        Gets the id of this OpsiConfiguration.
        `OCID`__ of OPSI configuration resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this OpsiConfiguration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OpsiConfiguration.
        `OCID`__ of OPSI configuration resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this OpsiConfiguration.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this OpsiConfiguration.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this OpsiConfiguration.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OpsiConfiguration.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this OpsiConfiguration.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def opsi_config_type(self):
        """
        **[Required]** Gets the opsi_config_type of this OpsiConfiguration.
        OPSI configuration type.

        Allowed values for this property are: "UX_CONFIGURATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The opsi_config_type of this OpsiConfiguration.
        :rtype: str
        """
        return self._opsi_config_type

    @opsi_config_type.setter
    def opsi_config_type(self, opsi_config_type):
        """
        Sets the opsi_config_type of this OpsiConfiguration.
        OPSI configuration type.


        :param opsi_config_type: The opsi_config_type of this OpsiConfiguration.
        :type: str
        """
        allowed_values = ["UX_CONFIGURATION"]
        if not value_allowed_none_or_none_sentinel(opsi_config_type, allowed_values):
            opsi_config_type = 'UNKNOWN_ENUM_VALUE'
        self._opsi_config_type = opsi_config_type

    @property
    def display_name(self):
        """
        Gets the display_name of this OpsiConfiguration.
        User-friendly display name for the OPSI configuration. The name does not have to be unique.


        :return: The display_name of this OpsiConfiguration.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OpsiConfiguration.
        User-friendly display name for the OPSI configuration. The name does not have to be unique.


        :param display_name: The display_name of this OpsiConfiguration.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this OpsiConfiguration.
        Description of OPSI configuration.


        :return: The description of this OpsiConfiguration.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OpsiConfiguration.
        Description of OPSI configuration.


        :param description: The description of this OpsiConfiguration.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OpsiConfiguration.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OpsiConfiguration.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OpsiConfiguration.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OpsiConfiguration.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OpsiConfiguration.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OpsiConfiguration.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OpsiConfiguration.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OpsiConfiguration.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OpsiConfiguration.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this OpsiConfiguration.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OpsiConfiguration.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this OpsiConfiguration.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def time_created(self):
        """
        Gets the time_created of this OpsiConfiguration.
        The time at which the resource was first created. An RFC3339 formatted datetime string


        :return: The time_created of this OpsiConfiguration.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OpsiConfiguration.
        The time at which the resource was first created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this OpsiConfiguration.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this OpsiConfiguration.
        The time at which the resource was last updated. An RFC3339 formatted datetime string


        :return: The time_updated of this OpsiConfiguration.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OpsiConfiguration.
        The time at which the resource was last updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this OpsiConfiguration.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this OpsiConfiguration.
        OPSI configuration resource lifecycle state.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OpsiConfiguration.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OpsiConfiguration.
        OPSI configuration resource lifecycle state.


        :param lifecycle_state: The lifecycle_state of this OpsiConfiguration.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this OpsiConfiguration.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this OpsiConfiguration.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this OpsiConfiguration.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this OpsiConfiguration.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def config_items(self):
        """
        Gets the config_items of this OpsiConfiguration.
        Array of configuration item summary objects.


        :return: The config_items of this OpsiConfiguration.
        :rtype: list[oci.opsi.models.OpsiConfigurationConfigurationItemSummary]
        """
        return self._config_items

    @config_items.setter
    def config_items(self, config_items):
        """
        Sets the config_items of this OpsiConfiguration.
        Array of configuration item summary objects.


        :param config_items: The config_items of this OpsiConfiguration.
        :type: list[oci.opsi.models.OpsiConfigurationConfigurationItemSummary]
        """
        self._config_items = config_items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other