"""JSON schema for detail card."""
from typing import List

from pydantic import BaseModel


class CleInSystemPipelines(BaseModel):
    """Class CleInSystemPipelines."""

    pipelineId: int
    name: str
    issuesTotal: str
    issuesRsolved: str
    pipelineStatus: str
    pipelineStatusDetails: str
    lastRunDate: str
    pipelineFailedStatus: str


class EaAcrossSystemPipelines(BaseModel):
    """Class EaAcrossSystemPipelines."""

    pipelineId: int
    name: str
    issuesTotal: str
    issuesRsolved: str
    pipelineStatus: str
    pipelineStatusDetails: str
    lastRunDate: str
    pipelineFailedStatus: str


class RloadersPipelines(BaseModel):
    """Class RloadersPipelines."""

    pipelineId: int
    name: str
    pipelineStatus: str
    pipelineStatusDetails: str
    lastRunDate: str
    pipelineFailedStatus: str


class CleInSystem(BaseModel):
    """Class CleInSystem."""

    title: str
    pipelines: List[CleInSystemPipelines]


class EaAcrossSystem(BaseModel):
    """Class EaAcrossSystem."""

    title: str
    pipelines: List[EaAcrossSystemPipelines]


class RLoaders(BaseModel):
    """Class RLoaders."""

    title: str
    pipelines: List[RloadersPipelines]


class PipelinesDetails(BaseModel):
    """Class PipelinesDetails."""

    cleInSystem: CleInSystem
    eaAcrossSystem: EaAcrossSystem
    rLoaders: RLoaders


class DetailCardResponse(BaseModel):
    """Class DetailCardResponse."""

    token: str
    refineryId: int
    refineryName: str
    pipelinsDetails: PipelinesDetails
