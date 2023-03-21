# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .build_runner_shape_config import BuildRunnerShapeConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomBuildRunnerShapeConfig(BuildRunnerShapeConfig):
    """
    Specifies the custom build runner shape config.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CustomBuildRunnerShapeConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.CustomBuildRunnerShapeConfig.build_runner_type` attribute
        of this class is ``CUSTOM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param build_runner_type:
            The value to assign to the build_runner_type property of this CustomBuildRunnerShapeConfig.
            Allowed values for this property are: "CUSTOM", "DEFAULT"
        :type build_runner_type: str

        :param ocpus:
            The value to assign to the ocpus property of this CustomBuildRunnerShapeConfig.
        :type ocpus: int

        :param memory_in_gbs:
            The value to assign to the memory_in_gbs property of this CustomBuildRunnerShapeConfig.
        :type memory_in_gbs: int

        """
        self.swagger_types = {
            'build_runner_type': 'str',
            'ocpus': 'int',
            'memory_in_gbs': 'int'
        }

        self.attribute_map = {
            'build_runner_type': 'buildRunnerType',
            'ocpus': 'ocpus',
            'memory_in_gbs': 'memoryInGBs'
        }

        self._build_runner_type = None
        self._ocpus = None
        self._memory_in_gbs = None
        self._build_runner_type = 'CUSTOM'

    @property
    def ocpus(self):
        """
        **[Required]** Gets the ocpus of this CustomBuildRunnerShapeConfig.
        The total number of OCPUs set for the instance.


        :return: The ocpus of this CustomBuildRunnerShapeConfig.
        :rtype: int
        """
        return self._ocpus

    @ocpus.setter
    def ocpus(self, ocpus):
        """
        Sets the ocpus of this CustomBuildRunnerShapeConfig.
        The total number of OCPUs set for the instance.


        :param ocpus: The ocpus of this CustomBuildRunnerShapeConfig.
        :type: int
        """
        self._ocpus = ocpus

    @property
    def memory_in_gbs(self):
        """
        **[Required]** Gets the memory_in_gbs of this CustomBuildRunnerShapeConfig.
        The total amount of memory set for the instance in gigabytes.


        :return: The memory_in_gbs of this CustomBuildRunnerShapeConfig.
        :rtype: int
        """
        return self._memory_in_gbs

    @memory_in_gbs.setter
    def memory_in_gbs(self, memory_in_gbs):
        """
        Sets the memory_in_gbs of this CustomBuildRunnerShapeConfig.
        The total amount of memory set for the instance in gigabytes.


        :param memory_in_gbs: The memory_in_gbs of this CustomBuildRunnerShapeConfig.
        :type: int
        """
        self._memory_in_gbs = memory_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
