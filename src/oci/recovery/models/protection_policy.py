# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProtectionPolicy(object):
    """
    The details of a protection policy.A policy defines the exact number of days to retain protected database backups created by Recovery Service.
    Each protected database must be associated with one protection policy. You can use Oracle-defined protection policies or create custom policies to suit your internal backup storage regulation demands.
    """

    #: A constant which can be used with the lifecycle_state property of a ProtectionPolicy.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ProtectionPolicy.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ProtectionPolicy.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ProtectionPolicy.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ProtectionPolicy.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ProtectionPolicy.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ProtectionPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ProtectionPolicy.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ProtectionPolicy.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ProtectionPolicy.
        :type compartment_id: str

        :param backup_retention_period_in_days:
            The value to assign to the backup_retention_period_in_days property of this ProtectionPolicy.
        :type backup_retention_period_in_days: int

        :param is_predefined_policy:
            The value to assign to the is_predefined_policy property of this ProtectionPolicy.
        :type is_predefined_policy: bool

        :param time_created:
            The value to assign to the time_created property of this ProtectionPolicy.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ProtectionPolicy.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ProtectionPolicy.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ProtectionPolicy.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ProtectionPolicy.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ProtectionPolicy.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ProtectionPolicy.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'backup_retention_period_in_days': 'int',
            'is_predefined_policy': 'bool',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'backup_retention_period_in_days': 'backupRetentionPeriodInDays',
            'is_predefined_policy': 'isPredefinedPolicy',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._backup_retention_period_in_days = None
        self._is_predefined_policy = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ProtectionPolicy.
        The protection policy OCID.


        :return: The id of this ProtectionPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProtectionPolicy.
        The protection policy OCID.


        :param id: The id of this ProtectionPolicy.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this ProtectionPolicy.
        A user provided name for the protection policy.


        :return: The display_name of this ProtectionPolicy.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ProtectionPolicy.
        A user provided name for the protection policy.


        :param display_name: The display_name of this ProtectionPolicy.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ProtectionPolicy.
        The OCID of the compartment that contains the protection policy.


        :return: The compartment_id of this ProtectionPolicy.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ProtectionPolicy.
        The OCID of the compartment that contains the protection policy.


        :param compartment_id: The compartment_id of this ProtectionPolicy.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def backup_retention_period_in_days(self):
        """
        **[Required]** Gets the backup_retention_period_in_days of this ProtectionPolicy.
        The maximum number of days to retain backups for a protected database. Specify a period ranging from a minimum 14 days to a maximum 95 days. For example, specify the value 55 if you want to retain backups for 55 days.


        :return: The backup_retention_period_in_days of this ProtectionPolicy.
        :rtype: int
        """
        return self._backup_retention_period_in_days

    @backup_retention_period_in_days.setter
    def backup_retention_period_in_days(self, backup_retention_period_in_days):
        """
        Sets the backup_retention_period_in_days of this ProtectionPolicy.
        The maximum number of days to retain backups for a protected database. Specify a period ranging from a minimum 14 days to a maximum 95 days. For example, specify the value 55 if you want to retain backups for 55 days.


        :param backup_retention_period_in_days: The backup_retention_period_in_days of this ProtectionPolicy.
        :type: int
        """
        self._backup_retention_period_in_days = backup_retention_period_in_days

    @property
    def is_predefined_policy(self):
        """
        **[Required]** Gets the is_predefined_policy of this ProtectionPolicy.
        Set to TRUE if the policy is Oracle-defined, and FALSE for a user-defined custom policy. You can modify only the custom policies.


        :return: The is_predefined_policy of this ProtectionPolicy.
        :rtype: bool
        """
        return self._is_predefined_policy

    @is_predefined_policy.setter
    def is_predefined_policy(self, is_predefined_policy):
        """
        Sets the is_predefined_policy of this ProtectionPolicy.
        Set to TRUE if the policy is Oracle-defined, and FALSE for a user-defined custom policy. You can modify only the custom policies.


        :param is_predefined_policy: The is_predefined_policy of this ProtectionPolicy.
        :type: bool
        """
        self._is_predefined_policy = is_predefined_policy

    @property
    def time_created(self):
        """
        Gets the time_created of this ProtectionPolicy.
        An RFC3339 formatted datetime string that indicates the created time for the protection policy. For example: '2020-05-22T21:10:29.600Z'.


        :return: The time_created of this ProtectionPolicy.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ProtectionPolicy.
        An RFC3339 formatted datetime string that indicates the created time for the protection policy. For example: '2020-05-22T21:10:29.600Z'.


        :param time_created: The time_created of this ProtectionPolicy.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ProtectionPolicy.
        An RFC3339 formatted datetime string that indicates the updated time for the protection policy. For example: '2020-05-22T21:10:29.600Z'.


        :return: The time_updated of this ProtectionPolicy.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ProtectionPolicy.
        An RFC3339 formatted datetime string that indicates the updated time for the protection policy. For example: '2020-05-22T21:10:29.600Z'.


        :param time_updated: The time_updated of this ProtectionPolicy.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ProtectionPolicy.
        The current state of the protection policy. Allowed values are:
          - CREATING
          - UPDATING
          - ACTIVE
          - DELETING
          - DELETED
          - FAILED

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ProtectionPolicy.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ProtectionPolicy.
        The current state of the protection policy. Allowed values are:
          - CREATING
          - UPDATING
          - ACTIVE
          - DELETING
          - DELETED
          - FAILED


        :param lifecycle_state: The lifecycle_state of this ProtectionPolicy.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ProtectionPolicy.
        Detailed description about the current lifecycle state of the protection policy. For example, it can be used to provide actionable information for a resource in a Failed state.


        :return: The lifecycle_details of this ProtectionPolicy.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ProtectionPolicy.
        Detailed description about the current lifecycle state of the protection policy. For example, it can be used to provide actionable information for a resource in a Failed state.


        :param lifecycle_details: The lifecycle_details of this ProtectionPolicy.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ProtectionPolicy.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ProtectionPolicy.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ProtectionPolicy.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ProtectionPolicy.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ProtectionPolicy.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see `Resource Tags`__

        __ https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ProtectionPolicy.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ProtectionPolicy.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see `Resource Tags`__

        __ https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ProtectionPolicy.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ProtectionPolicy.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`. For more information, see `Resource Tags`__

        __ https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this ProtectionPolicy.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ProtectionPolicy.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`. For more information, see `Resource Tags`__

        __ https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this ProtectionPolicy.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other