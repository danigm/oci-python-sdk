# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MyDeviceAuthenticationFactors(object):
    """
    Authentication Factors
    """

    #: A constant which can be used with the type property of a MyDeviceAuthenticationFactors.
    #: This constant has a value of "EMAIL"
    TYPE_EMAIL = "EMAIL"

    #: A constant which can be used with the type property of a MyDeviceAuthenticationFactors.
    #: This constant has a value of "SMS"
    TYPE_SMS = "SMS"

    #: A constant which can be used with the type property of a MyDeviceAuthenticationFactors.
    #: This constant has a value of "TOTP"
    TYPE_TOTP = "TOTP"

    #: A constant which can be used with the type property of a MyDeviceAuthenticationFactors.
    #: This constant has a value of "PUSH"
    TYPE_PUSH = "PUSH"

    #: A constant which can be used with the type property of a MyDeviceAuthenticationFactors.
    #: This constant has a value of "OFFLINETOTP"
    TYPE_OFFLINETOTP = "OFFLINETOTP"

    #: A constant which can be used with the type property of a MyDeviceAuthenticationFactors.
    #: This constant has a value of "VOICE"
    TYPE_VOICE = "VOICE"

    #: A constant which can be used with the type property of a MyDeviceAuthenticationFactors.
    #: This constant has a value of "PHONE_CALL"
    TYPE_PHONE_CALL = "PHONE_CALL"

    #: A constant which can be used with the type property of a MyDeviceAuthenticationFactors.
    #: This constant has a value of "THIRDPARTY"
    TYPE_THIRDPARTY = "THIRDPARTY"

    #: A constant which can be used with the type property of a MyDeviceAuthenticationFactors.
    #: This constant has a value of "FIDO_AUTHENTICATOR"
    TYPE_FIDO_AUTHENTICATOR = "FIDO_AUTHENTICATOR"

    #: A constant which can be used with the type property of a MyDeviceAuthenticationFactors.
    #: This constant has a value of "YUBICO_OTP"
    TYPE_YUBICO_OTP = "YUBICO_OTP"

    #: A constant which can be used with the status property of a MyDeviceAuthenticationFactors.
    #: This constant has a value of "INITIATED"
    STATUS_INITIATED = "INITIATED"

    #: A constant which can be used with the status property of a MyDeviceAuthenticationFactors.
    #: This constant has a value of "INPROGRESS"
    STATUS_INPROGRESS = "INPROGRESS"

    #: A constant which can be used with the status property of a MyDeviceAuthenticationFactors.
    #: This constant has a value of "ENROLLED"
    STATUS_ENROLLED = "ENROLLED"

    #: A constant which can be used with the status property of a MyDeviceAuthenticationFactors.
    #: This constant has a value of "LOCKED"
    STATUS_LOCKED = "LOCKED"

    #: A constant which can be used with the status property of a MyDeviceAuthenticationFactors.
    #: This constant has a value of "INACTIVE"
    STATUS_INACTIVE = "INACTIVE"

    #: A constant which can be used with the status property of a MyDeviceAuthenticationFactors.
    #: This constant has a value of "BLOCKED"
    STATUS_BLOCKED = "BLOCKED"

    def __init__(self, **kwargs):
        """
        Initializes a new MyDeviceAuthenticationFactors object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this MyDeviceAuthenticationFactors.
            Allowed values for this property are: "EMAIL", "SMS", "TOTP", "PUSH", "OFFLINETOTP", "VOICE", "PHONE_CALL", "THIRDPARTY", "FIDO_AUTHENTICATOR", "YUBICO_OTP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param status:
            The value to assign to the status property of this MyDeviceAuthenticationFactors.
            Allowed values for this property are: "INITIATED", "INPROGRESS", "ENROLLED", "LOCKED", "INACTIVE", "BLOCKED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param public_key:
            The value to assign to the public_key property of this MyDeviceAuthenticationFactors.
        :type public_key: str

        """
        self.swagger_types = {
            'type': 'str',
            'status': 'str',
            'public_key': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'status': 'status',
            'public_key': 'publicKey'
        }

        self._type = None
        self._status = None
        self._public_key = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this MyDeviceAuthenticationFactors.
        Authentication Factor Type

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "EMAIL", "SMS", "TOTP", "PUSH", "OFFLINETOTP", "VOICE", "PHONE_CALL", "THIRDPARTY", "FIDO_AUTHENTICATOR", "YUBICO_OTP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this MyDeviceAuthenticationFactors.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MyDeviceAuthenticationFactors.
        Authentication Factor Type

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param type: The type of this MyDeviceAuthenticationFactors.
        :type: str
        """
        allowed_values = ["EMAIL", "SMS", "TOTP", "PUSH", "OFFLINETOTP", "VOICE", "PHONE_CALL", "THIRDPARTY", "FIDO_AUTHENTICATOR", "YUBICO_OTP"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def status(self):
        """
        Gets the status of this MyDeviceAuthenticationFactors.
        Authentication Factor Status

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "INITIATED", "INPROGRESS", "ENROLLED", "LOCKED", "INACTIVE", "BLOCKED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this MyDeviceAuthenticationFactors.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this MyDeviceAuthenticationFactors.
        Authentication Factor Status

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param status: The status of this MyDeviceAuthenticationFactors.
        :type: str
        """
        allowed_values = ["INITIATED", "INPROGRESS", "ENROLLED", "LOCKED", "INACTIVE", "BLOCKED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def public_key(self):
        """
        Gets the public_key of this MyDeviceAuthenticationFactors.
        Authentication Factor public key issued by client

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The public_key of this MyDeviceAuthenticationFactors.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """
        Sets the public_key of this MyDeviceAuthenticationFactors.
        Authentication Factor public key issued by client

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param public_key: The public_key of this MyDeviceAuthenticationFactors.
        :type: str
        """
        self._public_key = public_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other