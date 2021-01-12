# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .action import Action
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FaaSAction(Action):
    """
    An action that delivers to an Oracle Functions endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FaaSAction object with values from keyword arguments. The default value of the :py:attr:`~oci.events.models.FaaSAction.action_type` attribute
        of this class is ``FAAS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action_type:
            The value to assign to the action_type property of this FaaSAction.
            Allowed values for this property are: "ONS", "OSS", "FAAS"
        :type action_type: str

        :param id:
            The value to assign to the id property of this FaaSAction.
        :type id: str

        :param lifecycle_message:
            The value to assign to the lifecycle_message property of this FaaSAction.
        :type lifecycle_message: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this FaaSAction.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param is_enabled:
            The value to assign to the is_enabled property of this FaaSAction.
        :type is_enabled: bool

        :param description:
            The value to assign to the description property of this FaaSAction.
        :type description: str

        :param function_id:
            The value to assign to the function_id property of this FaaSAction.
        :type function_id: str

        """
        self.swagger_types = {
            'action_type': 'str',
            'id': 'str',
            'lifecycle_message': 'str',
            'lifecycle_state': 'str',
            'is_enabled': 'bool',
            'description': 'str',
            'function_id': 'str'
        }

        self.attribute_map = {
            'action_type': 'actionType',
            'id': 'id',
            'lifecycle_message': 'lifecycleMessage',
            'lifecycle_state': 'lifecycleState',
            'is_enabled': 'isEnabled',
            'description': 'description',
            'function_id': 'functionId'
        }

        self._action_type = None
        self._id = None
        self._lifecycle_message = None
        self._lifecycle_state = None
        self._is_enabled = None
        self._description = None
        self._function_id = None
        self._action_type = 'FAAS'

    @property
    def function_id(self):
        """
        Gets the function_id of this FaaSAction.
        The `OCID`__ of a Function hosted by Oracle Functions Service.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The function_id of this FaaSAction.
        :rtype: str
        """
        return self._function_id

    @function_id.setter
    def function_id(self, function_id):
        """
        Sets the function_id of this FaaSAction.
        The `OCID`__ of a Function hosted by Oracle Functions Service.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param function_id: The function_id of this FaaSAction.
        :type: str
        """
        self._function_id = function_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
