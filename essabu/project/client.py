"""Project module client."""

from __future__ import annotations

from typing import TYPE_CHECKING

from essabu.common.http_client import HttpClient

if TYPE_CHECKING:
    from essabu.project.api.projects import ProjectApi
    from essabu.project.api.tasks import TaskApi
    from essabu.project.api.milestones import MilestoneApi
    from essabu.project.api.resource_allocations import ResourceAllocationApi
    from essabu.project.api.task_comments import TaskCommentApi
    from essabu.project.api.reports import ReportApi


class ProjectClient:
    """Client for the Project module."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http
        self._projects: ProjectApi | None = None
        self._tasks: TaskApi | None = None
        self._milestones: MilestoneApi | None = None
        self._resource_allocations: ResourceAllocationApi | None = None
        self._task_comments: TaskCommentApi | None = None
        self._reports: ReportApi | None = None

    @property
    def projects(self) -> ProjectApi:
        if self._projects is None:
            from essabu.project.api.projects import ProjectApi
            self._projects = ProjectApi(self._http)
        return self._projects
    @property
    def tasks(self) -> TaskApi:
        if self._tasks is None:
            from essabu.project.api.tasks import TaskApi
            self._tasks = TaskApi(self._http)
        return self._tasks
    @property
    def milestones(self) -> MilestoneApi:
        if self._milestones is None:
            from essabu.project.api.milestones import MilestoneApi
            self._milestones = MilestoneApi(self._http)
        return self._milestones
    @property
    def resource_allocations(self) -> ResourceAllocationApi:
        if self._resource_allocations is None:
            from essabu.project.api.resource_allocations import ResourceAllocationApi
            self._resource_allocations = ResourceAllocationApi(self._http)
        return self._resource_allocations
    @property
    def task_comments(self) -> TaskCommentApi:
        if self._task_comments is None:
            from essabu.project.api.task_comments import TaskCommentApi
            self._task_comments = TaskCommentApi(self._http)
        return self._task_comments
    @property
    def reports(self) -> ReportApi:
        if self._reports is None:
            from essabu.project.api.reports import ReportApi
            self._reports = ReportApi(self._http)
        return self._reports
