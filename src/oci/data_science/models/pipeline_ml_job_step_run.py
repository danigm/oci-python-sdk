# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .pipeline_step_run import PipelineStepRun
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PipelineMLJobStepRun(PipelineStepRun):
    """
    Detail of each MLJobStepRun.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PipelineMLJobStepRun object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.PipelineMLJobStepRun.step_type` attribute
        of this class is ``ML_JOB`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param step_type:
            The value to assign to the step_type property of this PipelineMLJobStepRun.
            Allowed values for this property are: "ML_JOB", "CUSTOM_SCRIPT"
        :type step_type: str

        :param time_started:
            The value to assign to the time_started property of this PipelineMLJobStepRun.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this PipelineMLJobStepRun.
        :type time_finished: datetime

        :param step_name:
            The value to assign to the step_name property of this PipelineMLJobStepRun.
        :type step_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PipelineMLJobStepRun.
            Allowed values for this property are: "WAITING", "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "DELETED", "SKIPPED"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this PipelineMLJobStepRun.
        :type lifecycle_details: str

        :param job_run_id:
            The value to assign to the job_run_id property of this PipelineMLJobStepRun.
        :type job_run_id: str

        """
        self.swagger_types = {
            'step_type': 'str',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'step_name': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'job_run_id': 'str'
        }

        self.attribute_map = {
            'step_type': 'stepType',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'step_name': 'stepName',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'job_run_id': 'jobRunId'
        }

        self._step_type = None
        self._time_started = None
        self._time_finished = None
        self._step_name = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._job_run_id = None
        self._step_type = 'ML_JOB'

    @property
    def job_run_id(self):
        """
        Gets the job_run_id of this PipelineMLJobStepRun.
        The `OCID`__ of the job run triggered for this step run.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The job_run_id of this PipelineMLJobStepRun.
        :rtype: str
        """
        return self._job_run_id

    @job_run_id.setter
    def job_run_id(self, job_run_id):
        """
        Sets the job_run_id of this PipelineMLJobStepRun.
        The `OCID`__ of the job run triggered for this step run.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param job_run_id: The job_run_id of this PipelineMLJobStepRun.
        :type: str
        """
        self._job_run_id = job_run_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
