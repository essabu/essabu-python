"""Tests for the Project module."""

from __future__ import annotations

import httpx
import pytest
import respx

from essabu import Essabu


@pytest.fixture
def client():
    c = Essabu(api_key="test-key", tenant_id="t", base_url="https://api.test.com")
    yield c
    c.close()


class TestProjects:
    @respx.mock
    def test_list_projects(self, client):
        respx.get("https://api.test.com/api/project/projects").mock(
            return_value=httpx.Response(200, json={
                "data": [{"id": "prj-1"}],
                "total": 1, "page": 1, "pageSize": 25, "totalPages": 1,
            })
        )
        result = client.project.projects.list()
        assert len(result.data) == 1


class TestTasks:
    @respx.mock
    def test_create_task(self, client):
        respx.post("https://api.test.com/api/project/tasks").mock(
            return_value=httpx.Response(201, json={"id": "task-1", "title": "Implement SDK"})
        )
        result = client.project.tasks.create(title="Implement SDK", project_id="prj-1")
        assert result["title"] == "Implement SDK"
