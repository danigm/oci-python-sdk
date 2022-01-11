# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FunctionSignature(object):
    """
    The function signature can specify function paramaters and/or function return type.
    """

    #: A constant which can be used with the model_type property of a FunctionSignature.
    #: This constant has a value of "DIS_FUNCTION_SIGNATURE"
    MODEL_TYPE_DIS_FUNCTION_SIGNATURE = "DIS_FUNCTION_SIGNATURE"

    def __init__(self, **kwargs):
        """
        Initializes a new FunctionSignature object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this FunctionSignature.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this FunctionSignature.
            Allowed values for this property are: "DIS_FUNCTION_SIGNATURE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this FunctionSignature.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this FunctionSignature.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this FunctionSignature.
        :type name: str

        :param ret_type:
            The value to assign to the ret_type property of this FunctionSignature.
        :type ret_type: oci.data_integration.models.ConfiguredType

        :param arguments:
            The value to assign to the arguments property of this FunctionSignature.
        :type arguments: list[oci.data_integration.models.TypedObject]

        :param description:
            The value to assign to the description property of this FunctionSignature.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this FunctionSignature.
        :type object_status: int

        """
        self.swagger_types = {
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'ret_type': 'ConfiguredType',
            'arguments': 'list[TypedObject]',
            'description': 'str',
            'object_status': 'int'
        }

        self.attribute_map = {
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'ret_type': 'retType',
            'arguments': 'arguments',
            'description': 'description',
            'object_status': 'objectStatus'
        }

        self._key = None
        self._model_type = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._ret_type = None
        self._arguments = None
        self._description = None
        self._object_status = None

    @property
    def key(self):
        """
        Gets the key of this FunctionSignature.
        The key of the object.


        :return: The key of this FunctionSignature.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this FunctionSignature.
        The key of the object.


        :param key: The key of this FunctionSignature.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        Gets the model_type of this FunctionSignature.
        The type of the object.

        Allowed values for this property are: "DIS_FUNCTION_SIGNATURE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this FunctionSignature.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this FunctionSignature.
        The type of the object.


        :param model_type: The model_type of this FunctionSignature.
        :type: str
        """
        allowed_values = ["DIS_FUNCTION_SIGNATURE"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this FunctionSignature.
        The model version of an object.


        :return: The model_version of this FunctionSignature.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this FunctionSignature.
        The model version of an object.


        :param model_version: The model_version of this FunctionSignature.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this FunctionSignature.

        :return: The parent_ref of this FunctionSignature.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this FunctionSignature.

        :param parent_ref: The parent_ref of this FunctionSignature.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this FunctionSignature.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this FunctionSignature.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FunctionSignature.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this FunctionSignature.
        :type: str
        """
        self._name = name

    @property
    def ret_type(self):
        """
        Gets the ret_type of this FunctionSignature.

        :return: The ret_type of this FunctionSignature.
        :rtype: oci.data_integration.models.ConfiguredType
        """
        return self._ret_type

    @ret_type.setter
    def ret_type(self, ret_type):
        """
        Sets the ret_type of this FunctionSignature.

        :param ret_type: The ret_type of this FunctionSignature.
        :type: oci.data_integration.models.ConfiguredType
        """
        self._ret_type = ret_type

    @property
    def arguments(self):
        """
        Gets the arguments of this FunctionSignature.
        An array of function arguments.


        :return: The arguments of this FunctionSignature.
        :rtype: list[oci.data_integration.models.TypedObject]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """
        Sets the arguments of this FunctionSignature.
        An array of function arguments.


        :param arguments: The arguments of this FunctionSignature.
        :type: list[oci.data_integration.models.TypedObject]
        """
        self._arguments = arguments

    @property
    def description(self):
        """
        Gets the description of this FunctionSignature.
        Detailed description for the object.


        :return: The description of this FunctionSignature.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FunctionSignature.
        Detailed description for the object.


        :param description: The description of this FunctionSignature.
        :type: str
        """
        self._description = description

    @property
    def object_status(self):
        """
        Gets the object_status of this FunctionSignature.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this FunctionSignature.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this FunctionSignature.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this FunctionSignature.
        :type: int
        """
        self._object_status = object_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other