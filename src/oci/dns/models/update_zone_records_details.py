# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateZoneRecordsDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateZoneRecordsDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this UpdateZoneRecordsDetails.
        :type items: list[RecordDetails]

        """
        self.swagger_types = {
            'items': 'list[RecordDetails]'
        }

        self.attribute_map = {
            'items': 'items'
        }

        self._items = None

    @property
    def items(self):
        """
        Gets the items of this UpdateZoneRecordsDetails.

        :return: The items of this UpdateZoneRecordsDetails.
        :rtype: list[RecordDetails]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this UpdateZoneRecordsDetails.

        :param items: The items of this UpdateZoneRecordsDetails.
        :type: list[RecordDetails]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
