# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RequirementDetails(object):
    """
    Minimum memory required by this PBF. The user should use memory greater than or equal to this value
    while configuring the Function.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RequirementDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param min_memory_required_in_mbs:
            The value to assign to the min_memory_required_in_mbs property of this RequirementDetails.
        :type min_memory_required_in_mbs: int

        :param policies:
            The value to assign to the policies property of this RequirementDetails.
        :type policies: list[oci.functions.models.PolicyDetails]

        """
        self.swagger_types = {
            'min_memory_required_in_mbs': 'int',
            'policies': 'list[PolicyDetails]'
        }

        self.attribute_map = {
            'min_memory_required_in_mbs': 'minMemoryRequiredInMBs',
            'policies': 'policies'
        }

        self._min_memory_required_in_mbs = None
        self._policies = None

    @property
    def min_memory_required_in_mbs(self):
        """
        **[Required]** Gets the min_memory_required_in_mbs of this RequirementDetails.
        Minimum memory required by this PBF. The user should use memory greater than or equal to
        this value while configuring the Function.


        :return: The min_memory_required_in_mbs of this RequirementDetails.
        :rtype: int
        """
        return self._min_memory_required_in_mbs

    @min_memory_required_in_mbs.setter
    def min_memory_required_in_mbs(self, min_memory_required_in_mbs):
        """
        Sets the min_memory_required_in_mbs of this RequirementDetails.
        Minimum memory required by this PBF. The user should use memory greater than or equal to
        this value while configuring the Function.


        :param min_memory_required_in_mbs: The min_memory_required_in_mbs of this RequirementDetails.
        :type: int
        """
        self._min_memory_required_in_mbs = min_memory_required_in_mbs

    @property
    def policies(self):
        """
        Gets the policies of this RequirementDetails.
        List of policies required for this PBF execution.


        :return: The policies of this RequirementDetails.
        :rtype: list[oci.functions.models.PolicyDetails]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """
        Sets the policies of this RequirementDetails.
        List of policies required for this PBF execution.


        :param policies: The policies of this RequirementDetails.
        :type: list[oci.functions.models.PolicyDetails]
        """
        self._policies = policies

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
