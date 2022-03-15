# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDisApplicationDetails(object):
    """
    Properties used in application create operations.
    """

    #: A constant which can be used with the model_type property of a CreateDisApplicationDetails.
    #: This constant has a value of "INTEGRATION_APPLICATION"
    MODEL_TYPE_INTEGRATION_APPLICATION = "INTEGRATION_APPLICATION"

    #: A constant which can be used with the lifecycle_state property of a CreateDisApplicationDetails.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a CreateDisApplicationDetails.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CreateDisApplicationDetails.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a CreateDisApplicationDetails.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a CreateDisApplicationDetails.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a CreateDisApplicationDetails.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDisApplicationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this CreateDisApplicationDetails.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateDisApplicationDetails.
        :type model_version: str

        :param model_type:
            The value to assign to the model_type property of this CreateDisApplicationDetails.
            Allowed values for this property are: "INTEGRATION_APPLICATION"
        :type model_type: str

        :param name:
            The value to assign to the name property of this CreateDisApplicationDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateDisApplicationDetails.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this CreateDisApplicationDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateDisApplicationDetails.
        :type identifier: str

        :param display_name:
            The value to assign to the display_name property of this CreateDisApplicationDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDisApplicationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDisApplicationDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CreateDisApplicationDetails.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param source_application_info:
            The value to assign to the source_application_info property of this CreateDisApplicationDetails.
        :type source_application_info: oci.data_integration.models.CreateSourceApplicationInfo

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreateDisApplicationDetails.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        """
        self.swagger_types = {
            'key': 'str',
            'model_version': 'str',
            'model_type': 'str',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str',
            'source_application_info': 'CreateSourceApplicationInfo',
            'registry_metadata': 'RegistryMetadata'
        }

        self.attribute_map = {
            'key': 'key',
            'model_version': 'modelVersion',
            'model_type': 'modelType',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'lifecycle_state': 'lifecycleState',
            'source_application_info': 'sourceApplicationInfo',
            'registry_metadata': 'registryMetadata'
        }

        self._key = None
        self._model_version = None
        self._model_type = None
        self._name = None
        self._description = None
        self._object_status = None
        self._identifier = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._lifecycle_state = None
        self._source_application_info = None
        self._registry_metadata = None

    @property
    def key(self):
        """
        Gets the key of this CreateDisApplicationDetails.
        Currently not used on application creation. Reserved for future.


        :return: The key of this CreateDisApplicationDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CreateDisApplicationDetails.
        Currently not used on application creation. Reserved for future.


        :param key: The key of this CreateDisApplicationDetails.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this CreateDisApplicationDetails.
        The object's model version.


        :return: The model_version of this CreateDisApplicationDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this CreateDisApplicationDetails.
        The object's model version.


        :param model_version: The model_version of this CreateDisApplicationDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def model_type(self):
        """
        Gets the model_type of this CreateDisApplicationDetails.
        The type of the application.

        Allowed values for this property are: "INTEGRATION_APPLICATION"


        :return: The model_type of this CreateDisApplicationDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this CreateDisApplicationDetails.
        The type of the application.


        :param model_type: The model_type of this CreateDisApplicationDetails.
        :type: str
        """
        allowed_values = ["INTEGRATION_APPLICATION"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            raise ValueError(
                "Invalid value for `model_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._model_type = model_type

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateDisApplicationDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this CreateDisApplicationDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateDisApplicationDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this CreateDisApplicationDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateDisApplicationDetails.
        Detailed description for the object.


        :return: The description of this CreateDisApplicationDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDisApplicationDetails.
        Detailed description for the object.


        :param description: The description of this CreateDisApplicationDetails.
        :type: str
        """
        self._description = description

    @property
    def object_status(self):
        """
        Gets the object_status of this CreateDisApplicationDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this CreateDisApplicationDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this CreateDisApplicationDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this CreateDisApplicationDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        **[Required]** Gets the identifier of this CreateDisApplicationDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this CreateDisApplicationDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this CreateDisApplicationDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this CreateDisApplicationDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDisApplicationDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The display_name of this CreateDisApplicationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDisApplicationDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param display_name: The display_name of this CreateDisApplicationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDisApplicationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDisApplicationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDisApplicationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDisApplicationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDisApplicationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDisApplicationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDisApplicationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDisApplicationDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this CreateDisApplicationDetails.
        The current state of the workspace.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"


        :return: The lifecycle_state of this CreateDisApplicationDetails.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CreateDisApplicationDetails.
        The current state of the workspace.


        :param lifecycle_state: The lifecycle_state of this CreateDisApplicationDetails.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def source_application_info(self):
        """
        Gets the source_application_info of this CreateDisApplicationDetails.

        :return: The source_application_info of this CreateDisApplicationDetails.
        :rtype: oci.data_integration.models.CreateSourceApplicationInfo
        """
        return self._source_application_info

    @source_application_info.setter
    def source_application_info(self, source_application_info):
        """
        Sets the source_application_info of this CreateDisApplicationDetails.

        :param source_application_info: The source_application_info of this CreateDisApplicationDetails.
        :type: oci.data_integration.models.CreateSourceApplicationInfo
        """
        self._source_application_info = source_application_info

    @property
    def registry_metadata(self):
        """
        Gets the registry_metadata of this CreateDisApplicationDetails.

        :return: The registry_metadata of this CreateDisApplicationDetails.
        :rtype: oci.data_integration.models.RegistryMetadata
        """
        return self._registry_metadata

    @registry_metadata.setter
    def registry_metadata(self, registry_metadata):
        """
        Sets the registry_metadata of this CreateDisApplicationDetails.

        :param registry_metadata: The registry_metadata of this CreateDisApplicationDetails.
        :type: oci.data_integration.models.RegistryMetadata
        """
        self._registry_metadata = registry_metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
