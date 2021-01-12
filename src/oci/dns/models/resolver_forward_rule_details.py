# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .resolver_rule_details import ResolverRuleDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResolverForwardRuleDetails(ResolverRuleDetails):
    """
    ResolverForwardRuleDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResolverForwardRuleDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.dns.models.ResolverForwardRuleDetails.action` attribute
        of this class is ``FORWARD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param client_address_conditions:
            The value to assign to the client_address_conditions property of this ResolverForwardRuleDetails.
        :type client_address_conditions: list[str]

        :param qname_cover_conditions:
            The value to assign to the qname_cover_conditions property of this ResolverForwardRuleDetails.
        :type qname_cover_conditions: list[str]

        :param action:
            The value to assign to the action property of this ResolverForwardRuleDetails.
            Allowed values for this property are: "FORWARD"
        :type action: str

        :param destination_addresses:
            The value to assign to the destination_addresses property of this ResolverForwardRuleDetails.
        :type destination_addresses: list[str]

        :param source_endpoint_name:
            The value to assign to the source_endpoint_name property of this ResolverForwardRuleDetails.
        :type source_endpoint_name: str

        """
        self.swagger_types = {
            'client_address_conditions': 'list[str]',
            'qname_cover_conditions': 'list[str]',
            'action': 'str',
            'destination_addresses': 'list[str]',
            'source_endpoint_name': 'str'
        }

        self.attribute_map = {
            'client_address_conditions': 'clientAddressConditions',
            'qname_cover_conditions': 'qnameCoverConditions',
            'action': 'action',
            'destination_addresses': 'destinationAddresses',
            'source_endpoint_name': 'sourceEndpointName'
        }

        self._client_address_conditions = None
        self._qname_cover_conditions = None
        self._action = None
        self._destination_addresses = None
        self._source_endpoint_name = None
        self._action = 'FORWARD'

    @property
    def destination_addresses(self):
        """
        **[Required]** Gets the destination_addresses of this ResolverForwardRuleDetails.
        IP addresses to which queries should be forwarded. Currently limited to a single address.


        :return: The destination_addresses of this ResolverForwardRuleDetails.
        :rtype: list[str]
        """
        return self._destination_addresses

    @destination_addresses.setter
    def destination_addresses(self, destination_addresses):
        """
        Sets the destination_addresses of this ResolverForwardRuleDetails.
        IP addresses to which queries should be forwarded. Currently limited to a single address.


        :param destination_addresses: The destination_addresses of this ResolverForwardRuleDetails.
        :type: list[str]
        """
        self._destination_addresses = destination_addresses

    @property
    def source_endpoint_name(self):
        """
        **[Required]** Gets the source_endpoint_name of this ResolverForwardRuleDetails.
        Name of an endpoint, that is a sub-resource of the resolver, to use as the forwarding interface. The
        endpoint must have isForwarding set to true.


        :return: The source_endpoint_name of this ResolverForwardRuleDetails.
        :rtype: str
        """
        return self._source_endpoint_name

    @source_endpoint_name.setter
    def source_endpoint_name(self, source_endpoint_name):
        """
        Sets the source_endpoint_name of this ResolverForwardRuleDetails.
        Name of an endpoint, that is a sub-resource of the resolver, to use as the forwarding interface. The
        endpoint must have isForwarding set to true.


        :param source_endpoint_name: The source_endpoint_name of this ResolverForwardRuleDetails.
        :type: str
        """
        self._source_endpoint_name = source_endpoint_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
