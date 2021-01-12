# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateLogSavedSearchDetails(object):
    """
    The update details to update a log saved search.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateLogSavedSearchDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UpdateLogSavedSearchDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this UpdateLogSavedSearchDetails.
        :type description: str

        :param query:
            The value to assign to the query property of this UpdateLogSavedSearchDetails.
        :type query: str

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateLogSavedSearchDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateLogSavedSearchDetails.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'query': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'query': 'query',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._name = None
        self._description = None
        self._query = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def name(self):
        """
        Gets the name of this UpdateLogSavedSearchDetails.
        The user-friendly display name. This must be unique within the enclosing resource,
        and it's changeable. Avoid entering confidential information.


        :return: The name of this UpdateLogSavedSearchDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateLogSavedSearchDetails.
        The user-friendly display name. This must be unique within the enclosing resource,
        and it's changeable. Avoid entering confidential information.


        :param name: The name of this UpdateLogSavedSearchDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this UpdateLogSavedSearchDetails.
        Description for this resource.


        :return: The description of this UpdateLogSavedSearchDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateLogSavedSearchDetails.
        Description for this resource.


        :param description: The description of this UpdateLogSavedSearchDetails.
        :type: str
        """
        self._description = description

    @property
    def query(self):
        """
        Gets the query of this UpdateLogSavedSearchDetails.
        The search query that is saved.


        :return: The query of this UpdateLogSavedSearchDetails.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this UpdateLogSavedSearchDetails.
        The search query that is saved.


        :param query: The query of this UpdateLogSavedSearchDetails.
        :type: str
        """
        self._query = query

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateLogSavedSearchDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateLogSavedSearchDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateLogSavedSearchDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateLogSavedSearchDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateLogSavedSearchDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateLogSavedSearchDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateLogSavedSearchDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateLogSavedSearchDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
