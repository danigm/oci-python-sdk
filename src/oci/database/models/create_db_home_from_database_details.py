# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDbHomeFromDatabaseDetails(object):
    """
    Details for creating a Database Home if you are creating a database by restoring from a database backup.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDbHomeFromDatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDbHomeFromDatabaseDetails.
        :type display_name: str

        :param database:
            The value to assign to the database property of this CreateDbHomeFromDatabaseDetails.
        :type database: oci.database.models.CreateDatabaseFromAnotherDatabaseDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDbHomeFromDatabaseDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDbHomeFromDatabaseDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'database': 'CreateDatabaseFromAnotherDatabaseDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'database': 'database',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._database = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDbHomeFromDatabaseDetails.
        The user-provided name of the Database Home.


        :return: The display_name of this CreateDbHomeFromDatabaseDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDbHomeFromDatabaseDetails.
        The user-provided name of the Database Home.


        :param display_name: The display_name of this CreateDbHomeFromDatabaseDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def database(self):
        """
        **[Required]** Gets the database of this CreateDbHomeFromDatabaseDetails.

        :return: The database of this CreateDbHomeFromDatabaseDetails.
        :rtype: oci.database.models.CreateDatabaseFromAnotherDatabaseDetails
        """
        return self._database

    @database.setter
    def database(self, database):
        """
        Sets the database of this CreateDbHomeFromDatabaseDetails.

        :param database: The database of this CreateDbHomeFromDatabaseDetails.
        :type: oci.database.models.CreateDatabaseFromAnotherDatabaseDetails
        """
        self._database = database

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDbHomeFromDatabaseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDbHomeFromDatabaseDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDbHomeFromDatabaseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDbHomeFromDatabaseDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDbHomeFromDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDbHomeFromDatabaseDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDbHomeFromDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDbHomeFromDatabaseDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other