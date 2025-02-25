# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueueStats(object):
    """
    The stats for a queue and its dead letter queue.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new QueueStats object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param queue:
            The value to assign to the queue property of this QueueStats.
        :type queue: oci.queue.models.Stats

        :param dlq:
            The value to assign to the dlq property of this QueueStats.
        :type dlq: oci.queue.models.Stats

        """
        self.swagger_types = {
            'queue': 'Stats',
            'dlq': 'Stats'
        }

        self.attribute_map = {
            'queue': 'queue',
            'dlq': 'dlq'
        }

        self._queue = None
        self._dlq = None

    @property
    def queue(self):
        """
        **[Required]** Gets the queue of this QueueStats.

        :return: The queue of this QueueStats.
        :rtype: oci.queue.models.Stats
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """
        Sets the queue of this QueueStats.

        :param queue: The queue of this QueueStats.
        :type: oci.queue.models.Stats
        """
        self._queue = queue

    @property
    def dlq(self):
        """
        **[Required]** Gets the dlq of this QueueStats.

        :return: The dlq of this QueueStats.
        :rtype: oci.queue.models.Stats
        """
        return self._dlq

    @dlq.setter
    def dlq(self, dlq):
        """
        Sets the dlq of this QueueStats.

        :param dlq: The dlq of this QueueStats.
        :type: oci.queue.models.Stats
        """
        self._dlq = dlq

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
