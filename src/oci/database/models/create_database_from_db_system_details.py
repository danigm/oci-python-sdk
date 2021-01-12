# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDatabaseFromDbSystemDetails(object):
    """
    Details for creating a database by restoring from a source database system.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDatabaseFromDbSystemDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param admin_password:
            The value to assign to the admin_password property of this CreateDatabaseFromDbSystemDetails.
        :type admin_password: str

        :param db_name:
            The value to assign to the db_name property of this CreateDatabaseFromDbSystemDetails.
        :type db_name: str

        :param db_domain:
            The value to assign to the db_domain property of this CreateDatabaseFromDbSystemDetails.
        :type db_domain: str

        :param db_unique_name:
            The value to assign to the db_unique_name property of this CreateDatabaseFromDbSystemDetails.
        :type db_unique_name: str

        :param db_backup_config:
            The value to assign to the db_backup_config property of this CreateDatabaseFromDbSystemDetails.
        :type db_backup_config: oci.database.models.DbBackupConfig

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDatabaseFromDbSystemDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDatabaseFromDbSystemDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'admin_password': 'str',
            'db_name': 'str',
            'db_domain': 'str',
            'db_unique_name': 'str',
            'db_backup_config': 'DbBackupConfig',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'admin_password': 'adminPassword',
            'db_name': 'dbName',
            'db_domain': 'dbDomain',
            'db_unique_name': 'dbUniqueName',
            'db_backup_config': 'dbBackupConfig',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._admin_password = None
        self._db_name = None
        self._db_domain = None
        self._db_unique_name = None
        self._db_backup_config = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def admin_password(self):
        """
        **[Required]** Gets the admin_password of this CreateDatabaseFromDbSystemDetails.
        A strong password for SYS, SYSTEM, PDB Admin and TDE Wallet. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \\#, or -.


        :return: The admin_password of this CreateDatabaseFromDbSystemDetails.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """
        Sets the admin_password of this CreateDatabaseFromDbSystemDetails.
        A strong password for SYS, SYSTEM, PDB Admin and TDE Wallet. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \\#, or -.


        :param admin_password: The admin_password of this CreateDatabaseFromDbSystemDetails.
        :type: str
        """
        self._admin_password = admin_password

    @property
    def db_name(self):
        """
        Gets the db_name of this CreateDatabaseFromDbSystemDetails.
        The display name of the database to be created from the backup. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.


        :return: The db_name of this CreateDatabaseFromDbSystemDetails.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this CreateDatabaseFromDbSystemDetails.
        The display name of the database to be created from the backup. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.


        :param db_name: The db_name of this CreateDatabaseFromDbSystemDetails.
        :type: str
        """
        self._db_name = db_name

    @property
    def db_domain(self):
        """
        Gets the db_domain of this CreateDatabaseFromDbSystemDetails.
        The database domain. In a distributed database system, DB_DOMAIN specifies the logical location of the database within the network structure.


        :return: The db_domain of this CreateDatabaseFromDbSystemDetails.
        :rtype: str
        """
        return self._db_domain

    @db_domain.setter
    def db_domain(self, db_domain):
        """
        Sets the db_domain of this CreateDatabaseFromDbSystemDetails.
        The database domain. In a distributed database system, DB_DOMAIN specifies the logical location of the database within the network structure.


        :param db_domain: The db_domain of this CreateDatabaseFromDbSystemDetails.
        :type: str
        """
        self._db_domain = db_domain

    @property
    def db_unique_name(self):
        """
        Gets the db_unique_name of this CreateDatabaseFromDbSystemDetails.
        The `DB_UNIQUE_NAME` of the Oracle Database.


        :return: The db_unique_name of this CreateDatabaseFromDbSystemDetails.
        :rtype: str
        """
        return self._db_unique_name

    @db_unique_name.setter
    def db_unique_name(self, db_unique_name):
        """
        Sets the db_unique_name of this CreateDatabaseFromDbSystemDetails.
        The `DB_UNIQUE_NAME` of the Oracle Database.


        :param db_unique_name: The db_unique_name of this CreateDatabaseFromDbSystemDetails.
        :type: str
        """
        self._db_unique_name = db_unique_name

    @property
    def db_backup_config(self):
        """
        Gets the db_backup_config of this CreateDatabaseFromDbSystemDetails.

        :return: The db_backup_config of this CreateDatabaseFromDbSystemDetails.
        :rtype: oci.database.models.DbBackupConfig
        """
        return self._db_backup_config

    @db_backup_config.setter
    def db_backup_config(self, db_backup_config):
        """
        Sets the db_backup_config of this CreateDatabaseFromDbSystemDetails.

        :param db_backup_config: The db_backup_config of this CreateDatabaseFromDbSystemDetails.
        :type: oci.database.models.DbBackupConfig
        """
        self._db_backup_config = db_backup_config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDatabaseFromDbSystemDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDatabaseFromDbSystemDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDatabaseFromDbSystemDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDatabaseFromDbSystemDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDatabaseFromDbSystemDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDatabaseFromDbSystemDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDatabaseFromDbSystemDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDatabaseFromDbSystemDetails.
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
