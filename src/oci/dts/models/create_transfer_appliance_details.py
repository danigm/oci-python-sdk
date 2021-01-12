# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTransferApplianceDetails(object):
    """
    CreateTransferApplianceDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTransferApplianceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param customer_shipping_address:
            The value to assign to the customer_shipping_address property of this CreateTransferApplianceDetails.
        :type customer_shipping_address: oci.dts.models.ShippingAddress

        """
        self.swagger_types = {
            'customer_shipping_address': 'ShippingAddress'
        }

        self.attribute_map = {
            'customer_shipping_address': 'customerShippingAddress'
        }

        self._customer_shipping_address = None

    @property
    def customer_shipping_address(self):
        """
        Gets the customer_shipping_address of this CreateTransferApplianceDetails.

        :return: The customer_shipping_address of this CreateTransferApplianceDetails.
        :rtype: oci.dts.models.ShippingAddress
        """
        return self._customer_shipping_address

    @customer_shipping_address.setter
    def customer_shipping_address(self, customer_shipping_address):
        """
        Sets the customer_shipping_address of this CreateTransferApplianceDetails.

        :param customer_shipping_address: The customer_shipping_address of this CreateTransferApplianceDetails.
        :type: oci.dts.models.ShippingAddress
        """
        self._customer_shipping_address = customer_shipping_address

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
