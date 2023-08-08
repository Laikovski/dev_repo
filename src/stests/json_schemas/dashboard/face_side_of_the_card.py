"""Face side of the card."""
from typing import List

from pydantic import BaseModel


class IssuesDetails(BaseModel):
    """Model for Issues schema."""

    type: str
    issue_status_display_key: str
    no_of_issues: int


class ExecutionDetails(BaseModel):
    """Model for execution details schema."""

    last_executed_on: int
    status: str
    status_display_key: str
    last_error_message: str
    blocked_reason: str
    stages_details: dict
    issues_details: List[IssuesDetails]


class Pipelines(BaseModel):
    """Model for Pipeline details schema."""

    unique_identifier: str
    name: str
    display_order: int
    download_artifacts_api_link: str
    execution_details: ExecutionDetails


class PlantBreakdownStructureSummary(BaseModel):
    """Model for summary detail schema."""

    structure_summary_display_key: str
    value: int
    display_order: int
    issues_details: List[IssuesDetails]


class GroupsOfPipelines(BaseModel):
    """Model for groups pipeline schema."""

    unique_identifier: str
    display_key: str
    display_order: int
    pipelines: List[Pipelines]


class Site(BaseModel):
    """Model for site schema."""

    site_unique_identifier: str
    site_name: str


class DashboardCard(BaseModel):
    """Model for dashboard card schema."""

    unique_identifier: str
    name: str
    execution_details: ExecutionDetails
    site: Site
    plant_breakdown_structure_summary: List[PlantBreakdownStructureSummary]
    groups_of_pipelines: List[GroupsOfPipelines]
