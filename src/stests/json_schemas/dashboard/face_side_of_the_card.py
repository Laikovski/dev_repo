"""Face side of the card."""
from typing import Dict
from typing import List

from pydantic import BaseModel


class FaceCard(BaseModel):
    """Class FaceCard."""

    name: str
    refineryId: int
    details: Dict[str, int]
    issuesTotal: int
    issuesRsolved: int
    pipelineStatus: str
    pipelineStatusDetails: str
    lastRunDate: str
    pipelineFailedStatus: str


class AllowedRefinery(BaseModel):
    """Class AllowedRefinery."""

    name: str
    refineryId: int
    order: int


class APICardData(BaseModel):
    """APICardData."""

    token: str
    allowedRefinery: List[AllowedRefinery]
    refineryDetails: List[FaceCard]
