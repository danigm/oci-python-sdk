# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .operation import Operation
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OperationFromProcedure(Operation):
    """
    The operation object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OperationFromProcedure object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.OperationFromProcedure.model_type` attribute
        of this class is ``PROCEDURE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this OperationFromProcedure.
            Allowed values for this property are: "PROCEDURE"
        :type model_type: str

        :param metadata:
            The value to assign to the metadata property of this OperationFromProcedure.
        :type metadata: oci.data_connectivity.models.ObjectMetadata

        :param key:
            The value to assign to the key property of this OperationFromProcedure.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this OperationFromProcedure.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this OperationFromProcedure.
        :type parent_ref: oci.data_connectivity.models.ParentReference

        :param shape:
            The value to assign to the shape property of this OperationFromProcedure.
        :type shape: oci.data_connectivity.models.Shape

        :param name:
            The value to assign to the name property of this OperationFromProcedure.
        :type name: str

        :param object_version:
            The value to assign to the object_version property of this OperationFromProcedure.
        :type object_version: int

        :param external_key:
            The value to assign to the external_key property of this OperationFromProcedure.
        :type external_key: str

        :param resource_name:
            The value to assign to the resource_name property of this OperationFromProcedure.
        :type resource_name: str

        :param object_status:
            The value to assign to the object_status property of this OperationFromProcedure.
        :type object_status: int

        """
        self.swagger_types = {
            'model_type': 'str',
            'metadata': 'ObjectMetadata',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'shape': 'Shape',
            'name': 'str',
            'object_version': 'int',
            'external_key': 'str',
            'resource_name': 'str',
            'object_status': 'int'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'metadata': 'metadata',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'shape': 'shape',
            'name': 'name',
            'object_version': 'objectVersion',
            'external_key': 'externalKey',
            'resource_name': 'resourceName',
            'object_status': 'objectStatus'
        }

        self._model_type = None
        self._metadata = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._shape = None
        self._name = None
        self._object_version = None
        self._external_key = None
        self._resource_name = None
        self._object_status = None
        self._model_type = 'PROCEDURE'

    @property
    def key(self):
        """
        Gets the key of this OperationFromProcedure.
        The object key.


        :return: The key of this OperationFromProcedure.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this OperationFromProcedure.
        The object key.


        :param key: The key of this OperationFromProcedure.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this OperationFromProcedure.
        The model version of the object.


        :return: The model_version of this OperationFromProcedure.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this OperationFromProcedure.
        The model version of the object.


        :param model_version: The model_version of this OperationFromProcedure.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this OperationFromProcedure.

        :return: The parent_ref of this OperationFromProcedure.
        :rtype: oci.data_connectivity.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this OperationFromProcedure.

        :param parent_ref: The parent_ref of this OperationFromProcedure.
        :type: oci.data_connectivity.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def shape(self):
        """
        Gets the shape of this OperationFromProcedure.

        :return: The shape of this OperationFromProcedure.
        :rtype: oci.data_connectivity.models.Shape
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this OperationFromProcedure.

        :param shape: The shape of this OperationFromProcedure.
        :type: oci.data_connectivity.models.Shape
        """
        self._shape = shape

    @property
    def name(self):
        """
        Gets the name of this OperationFromProcedure.
        The operation name.


        :return: The name of this OperationFromProcedure.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OperationFromProcedure.
        The operation name.


        :param name: The name of this OperationFromProcedure.
        :type: str
        """
        self._name = name

    @property
    def object_version(self):
        """
        Gets the object_version of this OperationFromProcedure.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this OperationFromProcedure.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this OperationFromProcedure.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this OperationFromProcedure.
        :type: int
        """
        self._object_version = object_version

    @property
    def external_key(self):
        """
        Gets the external_key of this OperationFromProcedure.
        The external key for the object.


        :return: The external_key of this OperationFromProcedure.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this OperationFromProcedure.
        The external key for the object.


        :param external_key: The external_key of this OperationFromProcedure.
        :type: str
        """
        self._external_key = external_key

    @property
    def resource_name(self):
        """
        Gets the resource_name of this OperationFromProcedure.
        The resource name.


        :return: The resource_name of this OperationFromProcedure.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this OperationFromProcedure.
        The resource name.


        :param resource_name: The resource_name of this OperationFromProcedure.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def object_status(self):
        """
        Gets the object_status of this OperationFromProcedure.
        The status of an object that can be set to value 1 for shallow reference across objects, other values reserved.


        :return: The object_status of this OperationFromProcedure.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this OperationFromProcedure.
        The status of an object that can be set to value 1 for shallow reference across objects, other values reserved.


        :param object_status: The object_status of this OperationFromProcedure.
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
