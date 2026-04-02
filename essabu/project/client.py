"""Project module client for the Essabu SDK."""

from __future__ import annotations

from functools import cached_property

from essabu.common.http_client import HttpClient
from essabu.project.api.milestones import MilestonesApi
from essabu.project.api.projects import ProjectsApi
from essabu.project.api.reports import ReportsApi
from essabu.project.api.resource_allocations import ResourceAllocationsApi
from essabu.project.api.task_comments import TaskCommentsApi
from essabu.project.api.tasks import TasksApi


class ProjectClient:
    """Project module client providing access to all Project API resources."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    @cached_property
    def projects(self) -> ProjectsApi:
        return ProjectsApi(self._http)

    @cached_property
    def milestones(self) -> MilestonesApi:
        return MilestonesApi(self._http)

    @cached_property
    def tasks(self) -> TasksApi:
        return TasksApi(self._http)

    @cached_property
    def task_comments(self) -> TaskCommentsApi:
        return TaskCommentsApi(self._http)

    @cached_property
    def resource_allocations(self) -> ResourceAllocationsApi:
        return ResourceAllocationsApi(self._http)

    @cached_property
    def reports(self) -> ReportsApi:
        return ReportsApi(self._http)
