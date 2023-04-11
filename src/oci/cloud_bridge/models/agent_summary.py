# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AgentSummary(object):
    """
    Summary of the Agent.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AgentSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AgentSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this AgentSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AgentSummary.
        :type compartment_id: str

        :param agent_type:
            The value to assign to the agent_type property of this AgentSummary.
        :type agent_type: str

        :param agent_version:
            The value to assign to the agent_version property of this AgentSummary.
        :type agent_version: str

        :param os_version:
            The value to assign to the os_version property of this AgentSummary.
        :type os_version: str

        :param time_created:
            The value to assign to the time_created property of this AgentSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AgentSummary.
        :type time_updated: datetime

        :param time_last_sync_received:
            The value to assign to the time_last_sync_received property of this AgentSummary.
        :type time_last_sync_received: datetime

        :param heart_beat_status:
            The value to assign to the heart_beat_status property of this AgentSummary.
        :type heart_beat_status: str

        :param environment_id:
            The value to assign to the environment_id property of this AgentSummary.
        :type environment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AgentSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AgentSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AgentSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AgentSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this AgentSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'agent_type': 'str',
            'agent_version': 'str',
            'os_version': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_last_sync_received': 'datetime',
            'heart_beat_status': 'str',
            'environment_id': 'str',
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
            'agent_type': 'agentType',
            'agent_version': 'agentVersion',
            'os_version': 'osVersion',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_last_sync_received': 'timeLastSyncReceived',
            'heart_beat_status': 'heartBeatStatus',
            'environment_id': 'environmentId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._agent_type = None
        self._agent_version = None
        self._os_version = None
        self._time_created = None
        self._time_updated = None
        self._time_last_sync_received = None
        self._heart_beat_status = None
        self._environment_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AgentSummary.
        Unique identifier that is immutable on creation.


        :return: The id of this AgentSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AgentSummary.
        Unique identifier that is immutable on creation.


        :param id: The id of this AgentSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AgentSummary.
        Agent identifier, which can be renamed.


        :return: The display_name of this AgentSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AgentSummary.
        Agent identifier, which can be renamed.


        :param display_name: The display_name of this AgentSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AgentSummary.
        Compartment identifier.


        :return: The compartment_id of this AgentSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AgentSummary.
        Compartment identifier.


        :param compartment_id: The compartment_id of this AgentSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def agent_type(self):
        """
        **[Required]** Gets the agent_type of this AgentSummary.
        Type of Agent.


        :return: The agent_type of this AgentSummary.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        """
        Sets the agent_type of this AgentSummary.
        Type of Agent.


        :param agent_type: The agent_type of this AgentSummary.
        :type: str
        """
        self._agent_type = agent_type

    @property
    def agent_version(self):
        """
        **[Required]** Gets the agent_version of this AgentSummary.
        Agent identifier.


        :return: The agent_version of this AgentSummary.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """
        Sets the agent_version of this AgentSummary.
        Agent identifier.


        :param agent_version: The agent_version of this AgentSummary.
        :type: str
        """
        self._agent_version = agent_version

    @property
    def os_version(self):
        """
        **[Required]** Gets the os_version of this AgentSummary.
        OS version.


        :return: The os_version of this AgentSummary.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """
        Sets the os_version of this AgentSummary.
        OS version.


        :param os_version: The os_version of this AgentSummary.
        :type: str
        """
        self._os_version = os_version

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AgentSummary.
        The time when the Agent was created. An RFC3339 formatted datetime string.


        :return: The time_created of this AgentSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AgentSummary.
        The time when the Agent was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this AgentSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this AgentSummary.
        The time when the Agent was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this AgentSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AgentSummary.
        The time when the Agent was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this AgentSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_last_sync_received(self):
        """
        Gets the time_last_sync_received of this AgentSummary.
        The time when the last heartbeat of the Agent was noted. An RFC3339 formatted datetime string.


        :return: The time_last_sync_received of this AgentSummary.
        :rtype: datetime
        """
        return self._time_last_sync_received

    @time_last_sync_received.setter
    def time_last_sync_received(self, time_last_sync_received):
        """
        Sets the time_last_sync_received of this AgentSummary.
        The time when the last heartbeat of the Agent was noted. An RFC3339 formatted datetime string.


        :param time_last_sync_received: The time_last_sync_received of this AgentSummary.
        :type: datetime
        """
        self._time_last_sync_received = time_last_sync_received

    @property
    def heart_beat_status(self):
        """
        Gets the heart_beat_status of this AgentSummary.
        Current heartbeat status of the Agent based on its timeLastSyncReceived value.


        :return: The heart_beat_status of this AgentSummary.
        :rtype: str
        """
        return self._heart_beat_status

    @heart_beat_status.setter
    def heart_beat_status(self, heart_beat_status):
        """
        Sets the heart_beat_status of this AgentSummary.
        Current heartbeat status of the Agent based on its timeLastSyncReceived value.


        :param heart_beat_status: The heart_beat_status of this AgentSummary.
        :type: str
        """
        self._heart_beat_status = heart_beat_status

    @property
    def environment_id(self):
        """
        **[Required]** Gets the environment_id of this AgentSummary.
        Environment identifier.


        :return: The environment_id of this AgentSummary.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """
        Sets the environment_id of this AgentSummary.
        Environment identifier.


        :param environment_id: The environment_id of this AgentSummary.
        :type: str
        """
        self._environment_id = environment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AgentSummary.
        The current state of the Agent.


        :return: The lifecycle_state of this AgentSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AgentSummary.
        The current state of the Agent.


        :param lifecycle_state: The lifecycle_state of this AgentSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        **[Required]** Gets the lifecycle_details of this AgentSummary.
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this AgentSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AgentSummary.
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this AgentSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this AgentSummary.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this AgentSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AgentSummary.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this AgentSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this AgentSummary.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this AgentSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AgentSummary.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this AgentSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this AgentSummary.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this AgentSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this AgentSummary.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this AgentSummary.
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