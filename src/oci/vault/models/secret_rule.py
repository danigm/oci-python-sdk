# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecretRule(object):
    """
    A rule that you can apply to a secret to enforce certain conditions on the secret's usage and management.
    """

    #: A constant which can be used with the rule_type property of a SecretRule.
    #: This constant has a value of "SECRET_EXPIRY_RULE"
    RULE_TYPE_SECRET_EXPIRY_RULE = "SECRET_EXPIRY_RULE"

    #: A constant which can be used with the rule_type property of a SecretRule.
    #: This constant has a value of "SECRET_REUSE_RULE"
    RULE_TYPE_SECRET_REUSE_RULE = "SECRET_REUSE_RULE"

    def __init__(self, **kwargs):
        """
        Initializes a new SecretRule object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.vault.models.SecretExpiryRule`
        * :class:`~oci.vault.models.SecretReuseRule`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param rule_type:
            The value to assign to the rule_type property of this SecretRule.
            Allowed values for this property are: "SECRET_EXPIRY_RULE", "SECRET_REUSE_RULE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type rule_type: str

        """
        self.swagger_types = {
            'rule_type': 'str'
        }

        self.attribute_map = {
            'rule_type': 'ruleType'
        }

        self._rule_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['ruleType']

        if type == 'SECRET_EXPIRY_RULE':
            return 'SecretExpiryRule'

        if type == 'SECRET_REUSE_RULE':
            return 'SecretReuseRule'
        else:
            return 'SecretRule'

    @property
    def rule_type(self):
        """
        **[Required]** Gets the rule_type of this SecretRule.
        The type of rule, which either controls when the secret contents expire or whether they can be reused.

        Allowed values for this property are: "SECRET_EXPIRY_RULE", "SECRET_REUSE_RULE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The rule_type of this SecretRule.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """
        Sets the rule_type of this SecretRule.
        The type of rule, which either controls when the secret contents expire or whether they can be reused.


        :param rule_type: The rule_type of this SecretRule.
        :type: str
        """
        allowed_values = ["SECRET_EXPIRY_RULE", "SECRET_REUSE_RULE"]
        if not value_allowed_none_or_none_sentinel(rule_type, allowed_values):
            rule_type = 'UNKNOWN_ENUM_VALUE'
        self._rule_type = rule_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
