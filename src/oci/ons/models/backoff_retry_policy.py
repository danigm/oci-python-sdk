# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackoffRetryPolicy(object):
    """
    The backoff retry portion of the subscription delivery policy. For information about retry durations for subscriptions, see
    `How Notifications Works`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#how
    """

    #: A constant which can be used with the policy_type property of a BackoffRetryPolicy.
    #: This constant has a value of "EXPONENTIAL"
    POLICY_TYPE_EXPONENTIAL = "EXPONENTIAL"

    def __init__(self, **kwargs):
        """
        Initializes a new BackoffRetryPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param max_retry_duration:
            The value to assign to the max_retry_duration property of this BackoffRetryPolicy.
        :type max_retry_duration: int

        :param policy_type:
            The value to assign to the policy_type property of this BackoffRetryPolicy.
            Allowed values for this property are: "EXPONENTIAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type policy_type: str

        """
        self.swagger_types = {
            'max_retry_duration': 'int',
            'policy_type': 'str'
        }

        self.attribute_map = {
            'max_retry_duration': 'maxRetryDuration',
            'policy_type': 'policyType'
        }

        self._max_retry_duration = None
        self._policy_type = None

    @property
    def max_retry_duration(self):
        """
        **[Required]** Gets the max_retry_duration of this BackoffRetryPolicy.
        The maximum retry duration in milliseconds. Default value is `7200000` (2 hours).


        :return: The max_retry_duration of this BackoffRetryPolicy.
        :rtype: int
        """
        return self._max_retry_duration

    @max_retry_duration.setter
    def max_retry_duration(self, max_retry_duration):
        """
        Sets the max_retry_duration of this BackoffRetryPolicy.
        The maximum retry duration in milliseconds. Default value is `7200000` (2 hours).


        :param max_retry_duration: The max_retry_duration of this BackoffRetryPolicy.
        :type: int
        """
        self._max_retry_duration = max_retry_duration

    @property
    def policy_type(self):
        """
        **[Required]** Gets the policy_type of this BackoffRetryPolicy.
        The type of delivery policy.

        Allowed values for this property are: "EXPONENTIAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The policy_type of this BackoffRetryPolicy.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """
        Sets the policy_type of this BackoffRetryPolicy.
        The type of delivery policy.


        :param policy_type: The policy_type of this BackoffRetryPolicy.
        :type: str
        """
        allowed_values = ["EXPONENTIAL"]
        if not value_allowed_none_or_none_sentinel(policy_type, allowed_values):
            policy_type = 'UNKNOWN_ENUM_VALUE'
        self._policy_type = policy_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
