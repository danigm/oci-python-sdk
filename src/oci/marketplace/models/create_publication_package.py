# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePublicationPackage(object):
    """
    A base object for the properties of the package
    """

    #: A constant which can be used with the package_type property of a CreatePublicationPackage.
    #: This constant has a value of "ORCHESTRATION"
    PACKAGE_TYPE_ORCHESTRATION = "ORCHESTRATION"

    #: A constant which can be used with the package_type property of a CreatePublicationPackage.
    #: This constant has a value of "IMAGE"
    PACKAGE_TYPE_IMAGE = "IMAGE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePublicationPackage object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.marketplace.models.CreateImagePublicationPackage`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param package_version:
            The value to assign to the package_version property of this CreatePublicationPackage.
        :type package_version: str

        :param package_type:
            The value to assign to the package_type property of this CreatePublicationPackage.
            Allowed values for this property are: "ORCHESTRATION", "IMAGE"
        :type package_type: str

        :param operating_system:
            The value to assign to the operating_system property of this CreatePublicationPackage.
        :type operating_system: oci.marketplace.models.OperatingSystem

        :param eula:
            The value to assign to the eula property of this CreatePublicationPackage.
        :type eula: list[oci.marketplace.models.Eula]

        """
        self.swagger_types = {
            'package_version': 'str',
            'package_type': 'str',
            'operating_system': 'OperatingSystem',
            'eula': 'list[Eula]'
        }

        self.attribute_map = {
            'package_version': 'packageVersion',
            'package_type': 'packageType',
            'operating_system': 'operatingSystem',
            'eula': 'eula'
        }

        self._package_version = None
        self._package_type = None
        self._operating_system = None
        self._eula = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['packageType']

        if type == 'IMAGE':
            return 'CreateImagePublicationPackage'
        else:
            return 'CreatePublicationPackage'

    @property
    def package_version(self):
        """
        **[Required]** Gets the package_version of this CreatePublicationPackage.
        The version of the package


        :return: The package_version of this CreatePublicationPackage.
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """
        Sets the package_version of this CreatePublicationPackage.
        The version of the package


        :param package_version: The package_version of this CreatePublicationPackage.
        :type: str
        """
        self._package_version = package_version

    @property
    def package_type(self):
        """
        **[Required]** Gets the package_type of this CreatePublicationPackage.
        Type of the artifact of the listing

        Allowed values for this property are: "ORCHESTRATION", "IMAGE"


        :return: The package_type of this CreatePublicationPackage.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this CreatePublicationPackage.
        Type of the artifact of the listing


        :param package_type: The package_type of this CreatePublicationPackage.
        :type: str
        """
        allowed_values = ["ORCHESTRATION", "IMAGE"]
        if not value_allowed_none_or_none_sentinel(package_type, allowed_values):
            raise ValueError(
                "Invalid value for `package_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._package_type = package_type

    @property
    def operating_system(self):
        """
        **[Required]** Gets the operating_system of this CreatePublicationPackage.

        :return: The operating_system of this CreatePublicationPackage.
        :rtype: oci.marketplace.models.OperatingSystem
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """
        Sets the operating_system of this CreatePublicationPackage.

        :param operating_system: The operating_system of this CreatePublicationPackage.
        :type: oci.marketplace.models.OperatingSystem
        """
        self._operating_system = operating_system

    @property
    def eula(self):
        """
        **[Required]** Gets the eula of this CreatePublicationPackage.
        End User License Agreeement that a consumer of this listing has to accept


        :return: The eula of this CreatePublicationPackage.
        :rtype: list[oci.marketplace.models.Eula]
        """
        return self._eula

    @eula.setter
    def eula(self, eula):
        """
        Sets the eula of this CreatePublicationPackage.
        End User License Agreeement that a consumer of this listing has to accept


        :param eula: The eula of this CreatePublicationPackage.
        :type: list[oci.marketplace.models.Eula]
        """
        self._eula = eula

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
