# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateIPSecConnectionTunnelDetails(object):
    """
    UpdateIPSecConnectionTunnelDetails model.
    """

    #: A constant which can be used with the routing property of a UpdateIPSecConnectionTunnelDetails.
    #: This constant has a value of "BGP"
    ROUTING_BGP = "BGP"

    #: A constant which can be used with the routing property of a UpdateIPSecConnectionTunnelDetails.
    #: This constant has a value of "STATIC"
    ROUTING_STATIC = "STATIC"

    #: A constant which can be used with the routing property of a UpdateIPSecConnectionTunnelDetails.
    #: This constant has a value of "POLICY"
    ROUTING_POLICY = "POLICY"

    #: A constant which can be used with the ike_version property of a UpdateIPSecConnectionTunnelDetails.
    #: This constant has a value of "V1"
    IKE_VERSION_V1 = "V1"

    #: A constant which can be used with the ike_version property of a UpdateIPSecConnectionTunnelDetails.
    #: This constant has a value of "V2"
    IKE_VERSION_V2 = "V2"

    #: A constant which can be used with the oracle_initiation property of a UpdateIPSecConnectionTunnelDetails.
    #: This constant has a value of "INITIATOR_OR_RESPONDER"
    ORACLE_INITIATION_INITIATOR_OR_RESPONDER = "INITIATOR_OR_RESPONDER"

    #: A constant which can be used with the oracle_initiation property of a UpdateIPSecConnectionTunnelDetails.
    #: This constant has a value of "RESPONDER_ONLY"
    ORACLE_INITIATION_RESPONDER_ONLY = "RESPONDER_ONLY"

    #: A constant which can be used with the nat_translation_enabled property of a UpdateIPSecConnectionTunnelDetails.
    #: This constant has a value of "ENABLED"
    NAT_TRANSLATION_ENABLED_ENABLED = "ENABLED"

    #: A constant which can be used with the nat_translation_enabled property of a UpdateIPSecConnectionTunnelDetails.
    #: This constant has a value of "DISABLED"
    NAT_TRANSLATION_ENABLED_DISABLED = "DISABLED"

    #: A constant which can be used with the nat_translation_enabled property of a UpdateIPSecConnectionTunnelDetails.
    #: This constant has a value of "AUTO"
    NAT_TRANSLATION_ENABLED_AUTO = "AUTO"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateIPSecConnectionTunnelDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateIPSecConnectionTunnelDetails.
        :type display_name: str

        :param routing:
            The value to assign to the routing property of this UpdateIPSecConnectionTunnelDetails.
            Allowed values for this property are: "BGP", "STATIC", "POLICY"
        :type routing: str

        :param ike_version:
            The value to assign to the ike_version property of this UpdateIPSecConnectionTunnelDetails.
            Allowed values for this property are: "V1", "V2"
        :type ike_version: str

        :param bgp_session_config:
            The value to assign to the bgp_session_config property of this UpdateIPSecConnectionTunnelDetails.
        :type bgp_session_config: oci.core.models.UpdateIPSecTunnelBgpSessionDetails

        :param oracle_initiation:
            The value to assign to the oracle_initiation property of this UpdateIPSecConnectionTunnelDetails.
            Allowed values for this property are: "INITIATOR_OR_RESPONDER", "RESPONDER_ONLY"
        :type oracle_initiation: str

        :param nat_translation_enabled:
            The value to assign to the nat_translation_enabled property of this UpdateIPSecConnectionTunnelDetails.
            Allowed values for this property are: "ENABLED", "DISABLED", "AUTO"
        :type nat_translation_enabled: str

        :param phase_one_config:
            The value to assign to the phase_one_config property of this UpdateIPSecConnectionTunnelDetails.
        :type phase_one_config: oci.core.models.PhaseOneConfigDetails

        :param phase_two_config:
            The value to assign to the phase_two_config property of this UpdateIPSecConnectionTunnelDetails.
        :type phase_two_config: oci.core.models.PhaseTwoConfigDetails

        :param dpd_config:
            The value to assign to the dpd_config property of this UpdateIPSecConnectionTunnelDetails.
        :type dpd_config: oci.core.models.DpdConfig

        :param encryption_domain_config:
            The value to assign to the encryption_domain_config property of this UpdateIPSecConnectionTunnelDetails.
        :type encryption_domain_config: oci.core.models.UpdateIPSecTunnelEncryptionDomainDetails

        """
        self.swagger_types = {
            'display_name': 'str',
            'routing': 'str',
            'ike_version': 'str',
            'bgp_session_config': 'UpdateIPSecTunnelBgpSessionDetails',
            'oracle_initiation': 'str',
            'nat_translation_enabled': 'str',
            'phase_one_config': 'PhaseOneConfigDetails',
            'phase_two_config': 'PhaseTwoConfigDetails',
            'dpd_config': 'DpdConfig',
            'encryption_domain_config': 'UpdateIPSecTunnelEncryptionDomainDetails'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'routing': 'routing',
            'ike_version': 'ikeVersion',
            'bgp_session_config': 'bgpSessionConfig',
            'oracle_initiation': 'oracleInitiation',
            'nat_translation_enabled': 'natTranslationEnabled',
            'phase_one_config': 'phaseOneConfig',
            'phase_two_config': 'phaseTwoConfig',
            'dpd_config': 'dpdConfig',
            'encryption_domain_config': 'encryptionDomainConfig'
        }

        self._display_name = None
        self._routing = None
        self._ike_version = None
        self._bgp_session_config = None
        self._oracle_initiation = None
        self._nat_translation_enabled = None
        self._phase_one_config = None
        self._phase_two_config = None
        self._dpd_config = None
        self._encryption_domain_config = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateIPSecConnectionTunnelDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateIPSecConnectionTunnelDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateIPSecConnectionTunnelDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateIPSecConnectionTunnelDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def routing(self):
        """
        Gets the routing of this UpdateIPSecConnectionTunnelDetails.
        The type of routing to use for this tunnel (BGP dynamic routing, static routing, or policy-based routing).

        Allowed values for this property are: "BGP", "STATIC", "POLICY"


        :return: The routing of this UpdateIPSecConnectionTunnelDetails.
        :rtype: str
        """
        return self._routing

    @routing.setter
    def routing(self, routing):
        """
        Sets the routing of this UpdateIPSecConnectionTunnelDetails.
        The type of routing to use for this tunnel (BGP dynamic routing, static routing, or policy-based routing).


        :param routing: The routing of this UpdateIPSecConnectionTunnelDetails.
        :type: str
        """
        allowed_values = ["BGP", "STATIC", "POLICY"]
        if not value_allowed_none_or_none_sentinel(routing, allowed_values):
            raise ValueError(
                "Invalid value for `routing`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._routing = routing

    @property
    def ike_version(self):
        """
        Gets the ike_version of this UpdateIPSecConnectionTunnelDetails.
        Internet Key Exchange protocol version.

        Allowed values for this property are: "V1", "V2"


        :return: The ike_version of this UpdateIPSecConnectionTunnelDetails.
        :rtype: str
        """
        return self._ike_version

    @ike_version.setter
    def ike_version(self, ike_version):
        """
        Sets the ike_version of this UpdateIPSecConnectionTunnelDetails.
        Internet Key Exchange protocol version.


        :param ike_version: The ike_version of this UpdateIPSecConnectionTunnelDetails.
        :type: str
        """
        allowed_values = ["V1", "V2"]
        if not value_allowed_none_or_none_sentinel(ike_version, allowed_values):
            raise ValueError(
                "Invalid value for `ike_version`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._ike_version = ike_version

    @property
    def bgp_session_config(self):
        """
        Gets the bgp_session_config of this UpdateIPSecConnectionTunnelDetails.

        :return: The bgp_session_config of this UpdateIPSecConnectionTunnelDetails.
        :rtype: oci.core.models.UpdateIPSecTunnelBgpSessionDetails
        """
        return self._bgp_session_config

    @bgp_session_config.setter
    def bgp_session_config(self, bgp_session_config):
        """
        Sets the bgp_session_config of this UpdateIPSecConnectionTunnelDetails.

        :param bgp_session_config: The bgp_session_config of this UpdateIPSecConnectionTunnelDetails.
        :type: oci.core.models.UpdateIPSecTunnelBgpSessionDetails
        """
        self._bgp_session_config = bgp_session_config

    @property
    def oracle_initiation(self):
        """
        Gets the oracle_initiation of this UpdateIPSecConnectionTunnelDetails.
        Indicates whether the Oracle end of the IPSec connection is able to initiate starting up the IPSec tunnel.

        Allowed values for this property are: "INITIATOR_OR_RESPONDER", "RESPONDER_ONLY"


        :return: The oracle_initiation of this UpdateIPSecConnectionTunnelDetails.
        :rtype: str
        """
        return self._oracle_initiation

    @oracle_initiation.setter
    def oracle_initiation(self, oracle_initiation):
        """
        Sets the oracle_initiation of this UpdateIPSecConnectionTunnelDetails.
        Indicates whether the Oracle end of the IPSec connection is able to initiate starting up the IPSec tunnel.


        :param oracle_initiation: The oracle_initiation of this UpdateIPSecConnectionTunnelDetails.
        :type: str
        """
        allowed_values = ["INITIATOR_OR_RESPONDER", "RESPONDER_ONLY"]
        if not value_allowed_none_or_none_sentinel(oracle_initiation, allowed_values):
            raise ValueError(
                "Invalid value for `oracle_initiation`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._oracle_initiation = oracle_initiation

    @property
    def nat_translation_enabled(self):
        """
        Gets the nat_translation_enabled of this UpdateIPSecConnectionTunnelDetails.
        By default (the `AUTO` setting), IKE sends packets with a source and destination port set to 500,
        and when it detects that the port used to forward packets has changed (most likely because a NAT device
        is between the CPE device and the Oracle VPN headend) it will try to negotiate the use of NAT-T.

        The `ENABLED` option sets the IKE protocol to use port 4500 instead of 500 and forces encapsulating traffic with the ESP protocol inside UDP packets.

        The `DISABLED` option directs IKE to completely refuse to negotiate NAT-T
        even if it senses there may be a NAT device in use.

        Allowed values for this property are: "ENABLED", "DISABLED", "AUTO"


        :return: The nat_translation_enabled of this UpdateIPSecConnectionTunnelDetails.
        :rtype: str
        """
        return self._nat_translation_enabled

    @nat_translation_enabled.setter
    def nat_translation_enabled(self, nat_translation_enabled):
        """
        Sets the nat_translation_enabled of this UpdateIPSecConnectionTunnelDetails.
        By default (the `AUTO` setting), IKE sends packets with a source and destination port set to 500,
        and when it detects that the port used to forward packets has changed (most likely because a NAT device
        is between the CPE device and the Oracle VPN headend) it will try to negotiate the use of NAT-T.

        The `ENABLED` option sets the IKE protocol to use port 4500 instead of 500 and forces encapsulating traffic with the ESP protocol inside UDP packets.

        The `DISABLED` option directs IKE to completely refuse to negotiate NAT-T
        even if it senses there may be a NAT device in use.


        :param nat_translation_enabled: The nat_translation_enabled of this UpdateIPSecConnectionTunnelDetails.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "AUTO"]
        if not value_allowed_none_or_none_sentinel(nat_translation_enabled, allowed_values):
            raise ValueError(
                "Invalid value for `nat_translation_enabled`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._nat_translation_enabled = nat_translation_enabled

    @property
    def phase_one_config(self):
        """
        Gets the phase_one_config of this UpdateIPSecConnectionTunnelDetails.

        :return: The phase_one_config of this UpdateIPSecConnectionTunnelDetails.
        :rtype: oci.core.models.PhaseOneConfigDetails
        """
        return self._phase_one_config

    @phase_one_config.setter
    def phase_one_config(self, phase_one_config):
        """
        Sets the phase_one_config of this UpdateIPSecConnectionTunnelDetails.

        :param phase_one_config: The phase_one_config of this UpdateIPSecConnectionTunnelDetails.
        :type: oci.core.models.PhaseOneConfigDetails
        """
        self._phase_one_config = phase_one_config

    @property
    def phase_two_config(self):
        """
        Gets the phase_two_config of this UpdateIPSecConnectionTunnelDetails.

        :return: The phase_two_config of this UpdateIPSecConnectionTunnelDetails.
        :rtype: oci.core.models.PhaseTwoConfigDetails
        """
        return self._phase_two_config

    @phase_two_config.setter
    def phase_two_config(self, phase_two_config):
        """
        Sets the phase_two_config of this UpdateIPSecConnectionTunnelDetails.

        :param phase_two_config: The phase_two_config of this UpdateIPSecConnectionTunnelDetails.
        :type: oci.core.models.PhaseTwoConfigDetails
        """
        self._phase_two_config = phase_two_config

    @property
    def dpd_config(self):
        """
        Gets the dpd_config of this UpdateIPSecConnectionTunnelDetails.

        :return: The dpd_config of this UpdateIPSecConnectionTunnelDetails.
        :rtype: oci.core.models.DpdConfig
        """
        return self._dpd_config

    @dpd_config.setter
    def dpd_config(self, dpd_config):
        """
        Sets the dpd_config of this UpdateIPSecConnectionTunnelDetails.

        :param dpd_config: The dpd_config of this UpdateIPSecConnectionTunnelDetails.
        :type: oci.core.models.DpdConfig
        """
        self._dpd_config = dpd_config

    @property
    def encryption_domain_config(self):
        """
        Gets the encryption_domain_config of this UpdateIPSecConnectionTunnelDetails.

        :return: The encryption_domain_config of this UpdateIPSecConnectionTunnelDetails.
        :rtype: oci.core.models.UpdateIPSecTunnelEncryptionDomainDetails
        """
        return self._encryption_domain_config

    @encryption_domain_config.setter
    def encryption_domain_config(self, encryption_domain_config):
        """
        Sets the encryption_domain_config of this UpdateIPSecConnectionTunnelDetails.

        :param encryption_domain_config: The encryption_domain_config of this UpdateIPSecConnectionTunnelDetails.
        :type: oci.core.models.UpdateIPSecTunnelEncryptionDomainDetails
        """
        self._encryption_domain_config = encryption_domain_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
