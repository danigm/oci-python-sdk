# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RemoveVcnIpv6CidrDetails(object):
    """
    Details used when removing ULA or private IPv6 prefix or an IPv6 GUA assigned by Oracle or BYOIPv6 prefix. You can only remove one of these per request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RemoveVcnIpv6CidrDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ipv6_cidr_block:
            The value to assign to the ipv6_cidr_block property of this RemoveVcnIpv6CidrDetails.
        :type ipv6_cidr_block: str

        """
        self.swagger_types = {
            'ipv6_cidr_block': 'str'
        }

        self.attribute_map = {
            'ipv6_cidr_block': 'ipv6CidrBlock'
        }

        self._ipv6_cidr_block = None

    @property
    def ipv6_cidr_block(self):
        """
        Gets the ipv6_cidr_block of this RemoveVcnIpv6CidrDetails.
        This field is not required and should only be specified when removing ULA or private IPv6 prefix or an IPv6 GUA assigned by Oracle or BYOIPv6 prefix
        from a VCN's IPv6 address space.
        See`IPv6 Addresses`__.

        Example: `2001:0db8:0123::/56`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm


        :return: The ipv6_cidr_block of this RemoveVcnIpv6CidrDetails.
        :rtype: str
        """
        return self._ipv6_cidr_block

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, ipv6_cidr_block):
        """
        Sets the ipv6_cidr_block of this RemoveVcnIpv6CidrDetails.
        This field is not required and should only be specified when removing ULA or private IPv6 prefix or an IPv6 GUA assigned by Oracle or BYOIPv6 prefix
        from a VCN's IPv6 address space.
        See`IPv6 Addresses`__.

        Example: `2001:0db8:0123::/56`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm


        :param ipv6_cidr_block: The ipv6_cidr_block of this RemoveVcnIpv6CidrDetails.
        :type: str
        """
        self._ipv6_cidr_block = ipv6_cidr_block

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other