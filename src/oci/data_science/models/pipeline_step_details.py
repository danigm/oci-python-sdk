# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PipelineStepDetails(object):
    """
    A step in the pipeline.
    """

    #: A constant which can be used with the step_type property of a PipelineStepDetails.
    #: This constant has a value of "ML_JOB"
    STEP_TYPE_ML_JOB = "ML_JOB"

    #: A constant which can be used with the step_type property of a PipelineStepDetails.
    #: This constant has a value of "CUSTOM_SCRIPT"
    STEP_TYPE_CUSTOM_SCRIPT = "CUSTOM_SCRIPT"

    def __init__(self, **kwargs):
        """
        Initializes a new PipelineStepDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_science.models.PipelineMLJobStepDetails`
        * :class:`~oci.data_science.models.PipelineCustomScriptStepDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param step_type:
            The value to assign to the step_type property of this PipelineStepDetails.
            Allowed values for this property are: "ML_JOB", "CUSTOM_SCRIPT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type step_type: str

        :param step_name:
            The value to assign to the step_name property of this PipelineStepDetails.
        :type step_name: str

        :param description:
            The value to assign to the description property of this PipelineStepDetails.
        :type description: str

        :param depends_on:
            The value to assign to the depends_on property of this PipelineStepDetails.
        :type depends_on: list[str]

        :param step_configuration_details:
            The value to assign to the step_configuration_details property of this PipelineStepDetails.
        :type step_configuration_details: oci.data_science.models.PipelineStepConfigurationDetails

        """
        self.swagger_types = {
            'step_type': 'str',
            'step_name': 'str',
            'description': 'str',
            'depends_on': 'list[str]',
            'step_configuration_details': 'PipelineStepConfigurationDetails'
        }

        self.attribute_map = {
            'step_type': 'stepType',
            'step_name': 'stepName',
            'description': 'description',
            'depends_on': 'dependsOn',
            'step_configuration_details': 'stepConfigurationDetails'
        }

        self._step_type = None
        self._step_name = None
        self._description = None
        self._depends_on = None
        self._step_configuration_details = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['stepType']

        if type == 'ML_JOB':
            return 'PipelineMLJobStepDetails'

        if type == 'CUSTOM_SCRIPT':
            return 'PipelineCustomScriptStepDetails'
        else:
            return 'PipelineStepDetails'

    @property
    def step_type(self):
        """
        **[Required]** Gets the step_type of this PipelineStepDetails.
        The type of step.

        Allowed values for this property are: "ML_JOB", "CUSTOM_SCRIPT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The step_type of this PipelineStepDetails.
        :rtype: str
        """
        return self._step_type

    @step_type.setter
    def step_type(self, step_type):
        """
        Sets the step_type of this PipelineStepDetails.
        The type of step.


        :param step_type: The step_type of this PipelineStepDetails.
        :type: str
        """
        allowed_values = ["ML_JOB", "CUSTOM_SCRIPT"]
        if not value_allowed_none_or_none_sentinel(step_type, allowed_values):
            step_type = 'UNKNOWN_ENUM_VALUE'
        self._step_type = step_type

    @property
    def step_name(self):
        """
        **[Required]** Gets the step_name of this PipelineStepDetails.
        The name of the step. It must be unique within the pipeline. This is used to create the pipeline DAG.


        :return: The step_name of this PipelineStepDetails.
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        """
        Sets the step_name of this PipelineStepDetails.
        The name of the step. It must be unique within the pipeline. This is used to create the pipeline DAG.


        :param step_name: The step_name of this PipelineStepDetails.
        :type: str
        """
        self._step_name = step_name

    @property
    def description(self):
        """
        Gets the description of this PipelineStepDetails.
        A short description of the step.


        :return: The description of this PipelineStepDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PipelineStepDetails.
        A short description of the step.


        :param description: The description of this PipelineStepDetails.
        :type: str
        """
        self._description = description

    @property
    def depends_on(self):
        """
        Gets the depends_on of this PipelineStepDetails.
        The list of step names this current step depends on for execution.


        :return: The depends_on of this PipelineStepDetails.
        :rtype: list[str]
        """
        return self._depends_on

    @depends_on.setter
    def depends_on(self, depends_on):
        """
        Sets the depends_on of this PipelineStepDetails.
        The list of step names this current step depends on for execution.


        :param depends_on: The depends_on of this PipelineStepDetails.
        :type: list[str]
        """
        self._depends_on = depends_on

    @property
    def step_configuration_details(self):
        """
        Gets the step_configuration_details of this PipelineStepDetails.

        :return: The step_configuration_details of this PipelineStepDetails.
        :rtype: oci.data_science.models.PipelineStepConfigurationDetails
        """
        return self._step_configuration_details

    @step_configuration_details.setter
    def step_configuration_details(self, step_configuration_details):
        """
        Sets the step_configuration_details of this PipelineStepDetails.

        :param step_configuration_details: The step_configuration_details of this PipelineStepDetails.
        :type: oci.data_science.models.PipelineStepConfigurationDetails
        """
        self._step_configuration_details = step_configuration_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
