# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_connection_details import CreateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateConnectionFromObjectStorage(CreateConnectionDetails):
    """
    The details to create an Oracle Object Storage data asset connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateConnectionFromObjectStorage object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.CreateConnectionFromObjectStorage.model_type` attribute
        of this class is ``ORACLE_OBJECT_STORAGE_CONNECTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateConnectionFromObjectStorage.
            Allowed values for this property are: "ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION"
        :type model_type: str

        :param key:
            The value to assign to the key property of this CreateConnectionFromObjectStorage.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateConnectionFromObjectStorage.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this CreateConnectionFromObjectStorage.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this CreateConnectionFromObjectStorage.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateConnectionFromObjectStorage.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this CreateConnectionFromObjectStorage.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateConnectionFromObjectStorage.
        :type identifier: str

        :param connection_properties:
            The value to assign to the connection_properties property of this CreateConnectionFromObjectStorage.
        :type connection_properties: list[oci.data_integration.models.ConnectionProperty]

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreateConnectionFromObjectStorage.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        :param credential_file_content:
            The value to assign to the credential_file_content property of this CreateConnectionFromObjectStorage.
        :type credential_file_content: str

        :param user_id:
            The value to assign to the user_id property of this CreateConnectionFromObjectStorage.
        :type user_id: str

        :param finger_print:
            The value to assign to the finger_print property of this CreateConnectionFromObjectStorage.
        :type finger_print: str

        :param pass_phrase:
            The value to assign to the pass_phrase property of this CreateConnectionFromObjectStorage.
        :type pass_phrase: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'connection_properties': 'list[ConnectionProperty]',
            'registry_metadata': 'RegistryMetadata',
            'credential_file_content': 'str',
            'user_id': 'str',
            'finger_print': 'str',
            'pass_phrase': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'connection_properties': 'connectionProperties',
            'registry_metadata': 'registryMetadata',
            'credential_file_content': 'credentialFileContent',
            'user_id': 'userId',
            'finger_print': 'fingerPrint',
            'pass_phrase': 'passPhrase'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_status = None
        self._identifier = None
        self._connection_properties = None
        self._registry_metadata = None
        self._credential_file_content = None
        self._user_id = None
        self._finger_print = None
        self._pass_phrase = None
        self._model_type = 'ORACLE_OBJECT_STORAGE_CONNECTION'

    @property
    def credential_file_content(self):
        """
        Gets the credential_file_content of this CreateConnectionFromObjectStorage.
        The credential file content from an Oracle Object Storage wallet.


        :return: The credential_file_content of this CreateConnectionFromObjectStorage.
        :rtype: str
        """
        return self._credential_file_content

    @credential_file_content.setter
    def credential_file_content(self, credential_file_content):
        """
        Sets the credential_file_content of this CreateConnectionFromObjectStorage.
        The credential file content from an Oracle Object Storage wallet.


        :param credential_file_content: The credential_file_content of this CreateConnectionFromObjectStorage.
        :type: str
        """
        self._credential_file_content = credential_file_content

    @property
    def user_id(self):
        """
        Gets the user_id of this CreateConnectionFromObjectStorage.
        The OCI user OCID for the user to connect to.


        :return: The user_id of this CreateConnectionFromObjectStorage.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this CreateConnectionFromObjectStorage.
        The OCI user OCID for the user to connect to.


        :param user_id: The user_id of this CreateConnectionFromObjectStorage.
        :type: str
        """
        self._user_id = user_id

    @property
    def finger_print(self):
        """
        Gets the finger_print of this CreateConnectionFromObjectStorage.
        The fingerprint for the user.


        :return: The finger_print of this CreateConnectionFromObjectStorage.
        :rtype: str
        """
        return self._finger_print

    @finger_print.setter
    def finger_print(self, finger_print):
        """
        Sets the finger_print of this CreateConnectionFromObjectStorage.
        The fingerprint for the user.


        :param finger_print: The finger_print of this CreateConnectionFromObjectStorage.
        :type: str
        """
        self._finger_print = finger_print

    @property
    def pass_phrase(self):
        """
        Gets the pass_phrase of this CreateConnectionFromObjectStorage.
        The passphrase for the connection.


        :return: The pass_phrase of this CreateConnectionFromObjectStorage.
        :rtype: str
        """
        return self._pass_phrase

    @pass_phrase.setter
    def pass_phrase(self, pass_phrase):
        """
        Sets the pass_phrase of this CreateConnectionFromObjectStorage.
        The passphrase for the connection.


        :param pass_phrase: The pass_phrase of this CreateConnectionFromObjectStorage.
        :type: str
        """
        self._pass_phrase = pass_phrase

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other